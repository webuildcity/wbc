# -*- coding: utf-8 -*-
from rest_framework import viewsets

from models import *
from serializers import *

class MuncipalityViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MuncipalitySerializer
    queryset = Muncipality.objects.all()

class DistrictViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DistrictSerializer
    queryset = District.objects.all()

class QuarterViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = QuarterSerializer
    queryset = Quarter.objects.all()

class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
