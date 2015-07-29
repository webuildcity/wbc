# -*- coding: utf-8 -*-
from rest_framework import viewsets

from models import *
from serializers import *

class StakeholderViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StakeholderSerializer
    queryset = Stakeholder.objects.all()

class StakeholderRoleViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StakeholderRoleSerializer
    queryset = StakeholderRole.objects.all()

class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
