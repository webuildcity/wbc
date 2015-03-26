# -*- coding: utf-8 -*-
from rest_framework import viewsets

from models import *
from serializers import *

class MuncipalityViewSet(viewsets.ModelViewSet):
    serializer_class = MuncipalitySerializer
    queryset = Muncipality.objects.all()

class DistrictViewSet(viewsets.ModelViewSet):
    serializer_class = DistrictSerializer
    queryset = District.objects.all()

class QuarterViewSet(viewsets.ModelViewSet):
    serializer_class = QuarterSerializer
    queryset = Quarter.objects.all()

class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
