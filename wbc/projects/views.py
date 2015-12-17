# -*- coding: utf-8 -*-
import datetime
from django.conf import settings
from django.shortcuts import render,get_object_or_404
from django.core.urlresolvers import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed
from django.utils.decorators import method_decorator

from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.db.models import Q
from django.utils.timezone import now


from rest_framework import viewsets
from rest_framework.response import Response

from wbc.core.views import ProtectedCreateView, ProtectedUpdateView, ProtectedDeleteView
from wbc.region.models import District
from wbc.comments.models import Comment
from wbc.comments.forms import CommentForm
from wbc.events.models import Event, Date, Media, Publication
from wbc.process.models import ProcessType, ProcessStep
from models import *
from serializers import *

from guardian.shortcuts import assign_perm, get_perms

# from forms import *

class ProjectViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(request, queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(request, instance)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = Project.objects.all()
        active = self.request.query_params.get('active', None)

        if active is not None:
            queryset = queryset.filter(active=active)
        return queryset

    def get_serializer(self, request, queryset, **kwargs):
        geometry = self.request.query_params.get('geometry', None)

        if geometry == 'point':
            return ProjectPointSerializer(queryset, **kwargs)
        elif geometry == 'polygon':
            return ProjectPolygonSerializer(queryset, **kwargs)
        else:
            return ProjectSerializer(queryset, **kwargs)


class ListViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ListSerializer

    paginate_by = 25
    paginate_by_param = 'page_size'

    def get_queryset(self):
        queryset = Project.objects.all()

        search = self.request.query_params.get('search', None)
        if search is not None:
            queryset = queryset.filter(Q(identifier__icontains=search) | Q(address__icontains=search) | Q(entities__name__icontains=search))

        return queryset


class MapViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MapSerializer
    delta = now() - datetime.timedelta(days=100)
    queryset = Project.objects.all()

class ProjectCreate(ProtectedCreateView):
    model = Project
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save()

        user = User.objects.get(username=self.request.user)
        assign_perm('change_project', user, self.object) 
        assign_perm('delete_project', user, self.object) 

        url = self.object.get_absolute_url()
        return JsonResponse({'redirect':  url})

    def form_invalid(self, form):
        response = super(ProjectCreate, self).form_invalid(form)
        return response

class ProjectUpdate(ProtectedUpdateView):

    model = Project
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save()
        url = self.object.get_absolute_url()
        return JsonResponse({'redirect':  url})

    def form_invalid(self, form):
        response = super(ProjectUpdate, self).form_invalid(form)
        return response


class ProjectDelete(ProtectedDeleteView):
    model = Project

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):

        response = super(ProjectDelete, self).post(request, args, **kwargs)
        if self.request.is_ajax():
            response_data = {"redirect": '/'}
            return JsonResponse(response_data)
        else:
            return response

    def get_success_url(self):
        return "/"

def projects(request):
    return render(request,'projects/list.html',{'new_project_link': reverse('project_create')})

def project(request, pk):
    p = get_object_or_404(Project, id = int(pk))
    return project_request(request, p)

def projectslug(request, slug):
    p = Project.objects.get(slug__iexact=slug)
    return project_request(request, p)

def project_request(request, p):
    if request.method == 'POST':
        if len(request.POST["author_email1"]) == 0:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.enabled = True;
                comment.project = p
                comment.save()

    today = datetime.datetime.today()
    gallery = None
    if p.gallery:
        gallery = Gallery.objects.filter(slug = p.gallery.slug)

    processTypeList = None
    publications = p.publication_set.all()

    if publications:
        processTypeList = {}
        processTypes = ProcessType.objects.filter(process_steps__publication__project = p).distinct()
        processTypeList = list(processTypes)
        for proType in processTypeList:
            proType.process_steps2 = list(proType.process_steps.all())
            for step in proType.process_steps2:
                for pub in publications.filter(process_step = step):
                    step.publication = pub

    print p.publication_set.filter(begin__lte=today, end__gte=today)
    return render(request,'projects/details.html',{
        'project' : p,
        'comments': Comment.objects.filter(project = int(p.pk), enabled = True),
        'events'  : p.events.order_by('-begin'),
        'gallery' : gallery,
        'nextDate': p.events.filter(begin__gte=today, date__isnull=False).order_by('begin').first(),
        'lastNews': p.events.filter(media__isnull=False).order_by('begin').first(),
        'tags'    : p.tags.all(),
        'stakeholders' : p.stakeholders.all(),
        'processSteps': p.publication_set.filter(begin__lte=today, end__gte=today),
        # 'publications' : p.publication_set.all().order_by('process_step__process_type__name','process_step__order'),
        #'processSteps' : ProcessStep.objects.filter(publication_processsteps),
         'processTypes' : processTypeList,
         'following': p.stakeholders.filter(pk=request.user.profile.stakeholder.pk).exists()
    })


def follow(request, pk):
    p = get_object_or_404(Project, id = int(pk))
    if p.stakeholders.filter(pk=request.user.profile.stakeholder.pk).exists():
        p.stakeholders.remove(request.user.profile.stakeholder)
    else:
        p.stakeholders.add(request.user.profile.stakeholder)
    return JsonResponse({'redirect' : p.get_absolute_url()})