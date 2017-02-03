# -*- coding: utf-8 -*-
from serializers import *
from models import *
from rest_framework import viewsets

class StoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StorySerializer
    queryset = Story.objects.all()

class BaseStepViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BaseStepSerializer
    queryset = BaseStep.objects.all()

class AnchorViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AnchorSerializer
    queryset = Anchor.objects.all()


class SubstepViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SubstepSerializer
    queryset = Substep.objects.all()


class StoryListViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StoryListSerializer

    paginate_by = 25
    paginate_by_param = 'page_size'

    def get_queryset(self):
        queryset = Story.objects.all()

        # search = self.request.query_params.get('search', None)
        # if search is not None:
        #     queryset = queryset.filter(Q(identifier__icontains=search) | Q(address__icontains=search) | Q(entities__name__icontains=search))

        return queryset
