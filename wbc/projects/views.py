# -*- coding: utf-8 -*-
import datetime
from django.db import models

from datetime import timedelta
from django.conf import settings
from django.shortcuts import render,get_object_or_404
from django.core.urlresolvers import reverse,reverse_lazy
from django.core.exceptions import ValidationError

from django.db.models import Count, Sum

from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.models import User, Permission
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed
from django.utils.decorators import method_decorator

from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.db.models import Q
from django.utils.timezone import now


from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
import rest_framework_filters as filters
from rest_framework.response import Response
from rest_framework.decorators import api_view

from wbc.core.views import ProtectedCreateView, ProtectedUpdateView, ProtectedDeleteView
from wbc.region.models import District
# from wbc.comments.models import Comment
# from wbc.comments.forms import CommentForm
from wbc.events.models import Event, Date, Media, Publication
from wbc.process.models import ProcessType, ProcessStep
from wbc.notifications.models import Subscriber
from wbc.images.models import Photo, Album
from models import *

from wbc.rating.models import WbcRating
from wbc.tags.models import WbcTag

from serializers import *

from guardian.shortcuts import assign_perm, get_perms
from guardian.decorators import permission_required_or_403

from etherpad_lite import EtherpadLiteClient

class ProjectFilter(filters.FilterSet):

    class Meta:
        model = Project
        # fields = {'quarter' : "__all__"}
        fields = {'year': ['lt', 'lte', 'gt', 'gte', 'range']}


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_fields = ('name','year', 'id', 'typename')
    ordering_fields = ('name', 'year', 'id')
    ordering_filter = OrderingFilter()
    filter_class = ProjectFilter

    def get_serializer_class(self):

        geometry = self.request.query_params.get('geometry', None)

        if geometry == 'point':
            return ProjectPointSerializer
        elif geometry == 'polygon':
            return ProjectPolygonSerializer
        else:
            return ProjectSerializer

    def filter_queryset(self, queryset):
        queryset = super(ProjectViewSet, self).filter_queryset(queryset)
        return self.ordering_filter.filter_queryset(self.request, queryset, self)


# class ProjectGraphViewset():

# class ProjectViewSet(viewsets.GenericViewSet):
#     filter_fields = ('name', 'pk')


#     def list(self, request):
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(request, queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = self.get_queryset()
#         instance = get_object_or_404(queryset, pk=pk)
#         serializer = self.get_serializer(request, instance)
#         return Response(serializer.data)

#     def get_queryset(self):
#         queryset = Project.objects.filter(pk__lte=100)
#         active = self.request.query_params.get('active', None)

#         if active is not None:
#             queryset = queryset.filter(active=active)
#         return queryset

    # def get_serializer(self, request, queryset, **kwargs):
    #     geometry = self.request.query_params.get('geometry', None)

    #     if geometry == 'point':
    #         return ProjectPointSerializer(queryset, **kwargs)
    #     elif geometry == 'polygon':
    #         print "yooo"
    #         return ProjectPolygonSerializer(queryset, **kwargs)
    #     else:
    #         return ProjectSerializer(queryset, **kwargs)


@api_view(['GET', 'POST'])
def projects_data(request):

    # print request.query_params
    # baup = Project.objects.filter(tags__name__in=["Gartendenkmal"]).aggregate(Sum('area')

    feature = request.query_params.get('feature', None)
    entity = request.query_params.get('entity', None)
    aggregate = request.query_params.get('aggregate', None)
    sumFeature = request.query_params.get('sum', None)

    pros = Project.objects.filter(typename="Denkmal")

    if entity:
        pros = pros.filter(quarter=entity)

    resp = pros.values('year').annotate(c=Count('year')).order_by('year')

    currentYear = 1000
    steps = [1200,1400,1600,1800]
    returnData = []

    # while currentYear < 2010:
    for step in steps:
        if entity:
            returnData.append({"year" : currentYear , entity : len(pros.filter(year__gte=currentYear, year__lt=step).values('year').annotate(c=Count('year'))) })
        else:
            returnData.append({"year" : currentYear , "total" : len(pros.filter(year__gte=currentYear, year__lt=step).values('year').annotate(c=Count('year'))) })
        currentYear = step

    while currentYear < 2010:
        if entity:
            returnData.append({"year" : currentYear , entity : len(pros.filter(year__gte=currentYear, year__lt=currentYear+10).values('year').annotate(c=Count('year'))) })
        else:
            returnData.append({"year" : currentYear , "total" : len(pros.filter(year__gte=currentYear, year__lt=currentYear+10).values('year').annotate(c=Count('year'))) })
        currentYear+=10
    

    # pros = Project.objects.filter(typename="Denkmal").extra(select={
    #     'date_string_c': 'select count(*) from date_string',
    #     # 'news_like': 'select count(*) from tbl_news_likes where user_id=tbl_users.id'
    # }).\
    # values_list('first_name', 'last_name', 'guide_like','news_like')


    # for quart in quarts:
    #     if quart.polygon_gis:
    #         prosQuart = Project.objects.filter(typename="Denkmal", polygon_gis__intersects=quart.polygon_gis)
    #         respQuart = prosQuart.values('date_string').annotate(dist=Count('date_string')).order_by('-dist')
    #         print respQuart
    # events = Event.objects.all().annotate(paid_participants=models.Sum(
    #     models.Case(
    #         models.When(participant__is_paid=True, then=1),
    #         default=0, output_field=models.IntegerField()
    #     )))

    # for quart in quarts:
    #     print quart
    # #     # name = quart.name
    #     if quart.polygon_gis:
    #         prosQuart = Project.objects.filter(typename="Denkmal", polygon_gis__intersects=quart.polygon_gis)
    #         respQuart = prosQuart.values('date_string').annotate(quart=Count('date_string')).order_by('-quart')

    #         resp = quarts | prosQuart
    #     resp = resp.annotate(name = models.Sum(
    #             models.Case(
    #                 models.When(entities__name__in=quart.name, then=1),
    #                 default=0, output_field=models.IntegerField()
    #             )))

    return Response({"data": returnData})

    # if entity:
    #     try:
    #         ent = Entity.objects.get(name=entity)
    #     except Entity.DoesNotExist:
    #         ent = None
    #     if ent:
    #         pros = Project.objects.filter(polygon_gis__intersects=ent.polygon_gis)
    #     else:
    #         return Response({"data" : "Entity not found"})

    # if feature and aggregate:
    #     resp = pros.values(feature).annotate(c=Count(feature)).order_by(feature)
    #     return Response({"data": resp})

    # if feature and sumFeature:
    #     resp = pros.filter(tags__name__in=[feature]).aggregate(Sum(sumFeature))
    #     return Response({"data": resp})



    # if request.method == 'POST':
        # return Response({"message": "Got some data!", "data": request.data})
    # return Response({"message": "Hello, world!"})

# class DataViewSet(viewssets.ReadOnlyModelViewSet):
#     filter_fields = ('name','date_string', 'id')

#     typename = self.request.query_params.get('typename', None)

#     def get_queryset(self):
#         if (typename)
#         queryset = Project.objects.filter()


class ListViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ListSerializer
    # filter_backend = (filters.DjangoFilterBackend)
    filter_fields  = ('identifier', 'name')

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
    wbc_rated = None
    if request.user.is_authenticated():
        wbc_rated = WbcRating.objects.filter(project=p.pk, user=request.user.pk).exists()
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
            group = c.createGroupIfNotExistsFor(groupMapper=settings.PREFIX + str(p.pk))
            author = c.createAuthorIfNotExistsFor(authorMapper=settings.PREFIX + str(request.user))
            validUntil = now() + datetime.timedelta(hours=3)
            sessionID = c.createSession(groupID=unicode(group['groupID']), authorID=unicode(author['authorID']), validUntil=str(validUntil.strftime('%s')))
            sessionIDText = sessionID['sessionID']
        etherpadText = c.getText(padID=p.padId)['text']
        # etherpadText = c.getHTML(padID=p.padId)['html']
    
    important_tag = None
    if settings.GENERAL_CONTENT['wbcrating']:
        if len(p.tags.all().filter(important=True)) >0:
            important_tag = p.tags.all().filter(important=True)[0]


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
        'etherpad_url': settings.ETHERPAD_SETTINGS['base-url'],
        'session_id'  : sessionIDText,
        'important_tag': important_tag,
        'wbc_rated'    : wbc_rated,
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

# check if user is an organizer
def is_organizer(user):
    return user.groups.filter(name='organizer').exists()

# feature a project so it gets priorities
@login_required
@user_passes_test(is_organizer)
def feature(request, pk):
    p = get_object_or_404(Project, id = int(pk))
    if p.featured:
        p.featured = False
    else:
        p.featured = True
    p.save()

    return JsonResponse({'redirect' : p.get_absolute_url()})

# updown vote a project (once per project not per user)
@login_required
@user_passes_test(is_organizer)
def updownvote(request, pk, vote):
    p = get_object_or_404(Project, id = int(pk))
    if vote == "2":
        p.updownvote = True
    elif vote == "1":
        p.updownvote = False
    elif vote == "0":
        p.updownvote = None
    p.save()

    return JsonResponse({'redirect' : p.get_absolute_url()})


# wbc rating
@login_required
def wbc_rate(request, pk, user, tag):
    tagObj = WbcTag.objects.get(slug=tag)
    userObj = User.objects.get(pk=user)
    proObj = Project.objects.get(pk=pk)
    if not WbcRating.objects.filter(project=proObj, user=userObj, tag=tagObj).exists():
        rating = WbcRating(project=proObj, user=userObj, tag=tagObj)
        try:
            rating.clean()
            rating.save()
        except ValidationError as e:
            return JsonResponse({'error' : str(e)})
    else:
        WbcRating.objects.filter(project=proObj, user=userObj, tag=tagObj).delete()  
    return JsonResponse({'redirect' : proObj.get_absolute_url()})


#add or remove someone from blacklist
@login_required
@user_passes_test(is_organizer)
def blacklist(request, pk, user):
    p = get_object_or_404(Project, id = int(pk))
    userObj = get_object_or_404(User, id = int(user))
    if p.blacklist.filter(pk=user).exists():
        p.blacklist.remove(userObj)
    else:
        p.blacklist.add(userObj)
    p.save()
    return JsonResponse({'redirect' : p.get_absolute_url()})



#uploads a photo to a project, handles the creation of albums
def photo_upload(request, pk):

    project = get_object_or_404(Project, id= int(pk))
    # permission check, object and global permission needs to be checked seperated
    if request.user.has_perm('projects.change_project', project) or request.user.has_perm('projects.change_project'):
        created = False
        if project.album:
            album = project.album
        else:
            album = Album.objects.create()
            created = True
            album.save()
            project.album = album
            project.save()
        uploaded_file = request.FILES['file']
        photo = Photo.objects.create(album=album, file=uploaded_file)
        photo.save()
        project.save()
        response_dict = {
            'message': 'File uploaded successfully!',
            'thumbnail'     : photo.thumbnail.url ,
            'reload' : created
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

