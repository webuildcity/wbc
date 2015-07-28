# -*- coding: utf-8 -*-
from rest_framework import viewsets

from models import *
from serializers import *

class EventViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class DateViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()

class MediaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PublicationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PublicationSerializer
    queryset = Publication.objects.all()