
from rest_framework.reverse import reverse

from haystack import indexes
from models import Project

import json


class ProjectIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    description = indexes.CharField(model_attr='description')
    location = indexes.LocationField()
    polygon = indexes.CharField(model_attr='polygon', null=True)
    active = indexes.BooleanField(model_attr='active')
    tags = indexes.MultiValueField(faceted=True)
    entities = indexes.MultiValueField(faceted=True)
    internal_link = indexes.CharField()
    type = indexes.CharField()
    address_obj = indexes.CharField()
    thumbnail = indexes.CharField()
    content_auto = indexes.NgramField(use_template=True)
    num_stakeholder = indexes.IntegerField()
    created = indexes.DateField()
    created_by = indexes.CharField()
    teaser = indexes.CharField()
    ratings_avg = indexes.DecimalField()
    ratings_count = indexes.IntegerField()
    buffer_areas = indexes.MultiValueField()
    finished = indexes.DateField()
    isFinished = indexes.BooleanField(model_attr='isFinished', default=False)

    def get_model(self):
        return Project

    def prepare_tags(self, obj):
        return [tag.name for tag in obj.tags.all()]

    def prepare_entities(self, obj):
        return [ent.name for ent in obj.entities.all()]

    def prepare_buffer_areas(self, obj):
        return [json.loads(area.polygon) for area in obj.bufferarea_set.all()]
    
    def prepare_address_obj(self, obj):
        if obj.address_obj:
            return "%s %s" % (obj.address_obj.street, obj.address_obj.streetnumber)
        return None

    def prepare_location(self, obj):
        # If you're just storing the floats...
        if obj.lat:
            return "%s,%s" % (obj.lon, obj.lat)

    def prepare_type(self, obj):
        return 'project'

    def prepare_internal_link(self, obj):
        return obj.get_absolute_url()

    def prepare_thumbnail(self, obj):
        return obj.get_thumbnail_url()

    def prepare_num_stakeholder(self, obj):
        return obj.get_number_stakeholder()
    
    def prepare_created(self, obj):
        return obj.created

    def prepare_finished(self, obj):
        return obj.finished

    def prepare_created_by(self, obj):
        try:
            if obj.get_created_by():
                return obj.get_created_by().profile.full_name
            else:
                return None
        except:
            return None

    def prepare_ratings_avg(self, obj):
        if obj.ratings.values():
            return obj.ratings.values()[0]['average']
        return None

    def prepare_ratings_count(self, obj):
        if obj.ratings.values():
            return obj.ratings.values()[0]['count']
        return None

    def prepare_teaser(self, obj):
        return obj.get_teaser()

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()