# -*- coding: utf-8 -*-
import datetime
from datetime import timedelta
from django.conf import settings
from django.shortcuts import render,get_object_or_404
from django.core.urlresolvers import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Permission
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
# from wbc.comments.models import Comment
# from wbc.comments.forms import CommentForm
from wbc.events.models import Event, Date, Media, Publication
from wbc.process.models import ProcessType, ProcessStep
from wbc.notifications.models import Subscriber
from wbc.images.models import Photo, Album
from models import *

from serializers import *

from guardian.shortcuts import assign_perm, get_perms
from guardian.decorators import permission_required_or_403

from etherpad_lite import EtherpadLiteClient

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

    def dispatch(self, request, *args, **kwargs):
      #  print '%s.1add_%s' % (self.model._meta.app_label, self.model._meta.model_name)
        @login_required
        def wrapper(request, *args, **kwargs):
            return super(ProtectedCreateView, self).dispatch(request, *args, **kwargs)
        return wrapper(request, *args, **kwargs)

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
    # if request.method == 'POST':
    #     if len(request.POST["author_email1"]) == 0:
    #         form = CommentForm(request.POST)
    #         if form.is_valid():
    #             comment = form.save(commit=False)
    #             comment.enabled = True;
    #             comment.project = p
    #             comment.save()

    today = datetime.datetime.today()
    album = None
    try:
        if p.album:
            album = Photo.objects.filter(album= p.album)
    except:
        album = None
    processTypeList = None
    publications = p.publication_set.all()

    following = None
    if request.user.is_authenticated():
        following = p.stakeholders.filter(pk=request.user.profile.stakeholder.pk).exists()
    
    subscribed = None
    if request.user.is_authenticated() and request.user.profile.subscriber:
        subscribed = request.user.profile.subscriber.projects.filter(pk=p.pk).exists()

    if publications:
        processTypeList = {}
        processTypes = ProcessType.objects.filter(process_steps__publication__project = p).distinct()
        processTypeList = list(processTypes)
        for proType in processTypeList:
            proType.process_steps2 = list(proType.process_steps.all())
            for step in proType.process_steps2:
                for pub in publications.filter(process_step = step):
                    step.publication = pub

    etherpadText = ''
    sessionIDText = ''
    if p.padId and settings.DETAILS_TABS['etherpad']:
        c = EtherpadLiteClient(base_params={'apikey' : settings.ETHERPAD_SETTINGS['api_key'], 'baseUrl' : settings.ETHERPAD_SETTINGS['base-url'] + 'api'})
        if following:
            group = c.createGroupIfNotExistsFor(groupMapper=settings.PREFIX + p.slug)
            author = c.createAuthorIfNotExistsFor(authorMapper=settings.PREFIX + str(request.user))
            validUntil = now() + datetime.timedelta(hours=3)
            sessionID = c.createSession(groupID=unicode(group['groupID']), authorID=unicode(author['authorID']), validUntil=str(validUntil.strftime('%s')))
            sessionIDText = sessionID['sessionID']
        etherpadText = c.getHTML(padID=p.padId)['html']
        print p.padId
        print c.getText(padID=p.padId)

    response = render(request,'projects/details.html',{
        'project' : p,
        # 'comments': Comment.objects.filter(project = int(p.pk), enabled = True),
        'events'  : p.events.order_by('-begin'),
        'album' : album,
        'nextDate': p.events.filter(begin__gte=today, date__isnull=False).order_by('begin').first(),
        'lastNews': p.events.filter(media__isnull=False).order_by('begin').first(),
        'tags'    : p.tags.all(),
        'stakeholders' : p.stakeholders.all(),
        'processSteps': p.publication_set.filter(begin__lte=today, end__gte=today),
        # 'publications' : p.publication_set.all().order_by('process_step__process_type__name','process_step__order'),
        #'processSteps' : ProcessStep.objects.filter(publication_processsteps),
        'processTypes' : processTypeList,
        'following': following,
        'subscribed': subscribed,
        'bufferAreas' : p.bufferarea_set.all(),
        'attachments' : p.projectattachment_set.all(),
        'etherpadText': etherpadText,
        'tab_settings': settings.DETAILS_TABS,
        'etherpad_url': settings.ETHERPAD_SETTINGS['base-url'] + 'p/',
        'session_id'  : sessionIDText,
    })

    #create session id cookie for etherpad authentication
    if following and p.padId and settings.DETAILS_TABS['etherpad']:
        response.set_cookie('sessionID', sessionIDText)

    return response

@login_required
def follow(request, pk):
    p = get_object_or_404(Project, id = int(pk))
    if p.stakeholders.filter(pk=request.user.profile.stakeholder.pk).exists():
        p.stakeholders.remove(request.user.profile.stakeholder)
    else:
        p.stakeholders.add(request.user.profile.stakeholder)
    return JsonResponse({'redirect' : p.get_absolute_url()})

@login_required
def subscribe(request, pk):
    p = get_object_or_404(Project, id = int(pk))
    if not request.user.profile.subscriber:
        subscriber = Subscriber()
        subscriber.save()
        request.user.profile.subscriber = subscriber
        request.user.profile.save()
    if request.user.profile.subscriber.projects.filter(pk=int(pk)):
        request.user.profile.subscriber.projects.remove(p)
    else:
        request.user.profile.subscriber.projects.add(p)
    return JsonResponse({'redirect' : p.get_absolute_url()})



#uploads a photo to a project, handles the creation of albums
def photo_upload(request, pk):

    project = get_object_or_404(Project, id= int(pk))
    # permission check, object and global permission needs to be checked seperated
    if request.user.has_perm('projects.change_project', project) or request.user.has_perm('projects.change_project'):
        if project.album:
            album = project.album
        else:
            album = Album.objects.create()
            album.save()
            project.album = album
            project.save()
        uploaded_file = request.FILES['file']
        photo = Photo.objects.create(album=album, file=uploaded_file)
        photo.save()
        project.save()
        response_dict = {
            'message': 'File uploaded successfully!',
            'thumbnail'     : photo.thumbnail.url
        }

        return JsonResponse(response_dict)
    else:
        response_dict = {'message': 'No Permission!',}
        return JsonResponse(response_dict)

#deletes a photo from a project
def photo_delete(request, pk, photo):
    project = get_object_or_404(Project, id= int(pk))
    if request.user.has_perm('projects.change_project', project) or request.user.has_perm('projects.change_project'):
        photo = Photo.objects.filter(pk=photo, album=project.album)
        photo.delete()
        return JsonResponse({'message': 'deleted'})
    return JsonResponse({'message' : 'Error'})

