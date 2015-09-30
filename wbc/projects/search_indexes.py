import datetime
from haystack import indexes
from models import Project


class ProjectIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    description = indexes.CharField(model_attr='description')
    location = indexes.LocationField()
    tags = indexes.MultiValueField()
    link = indexes.CharField()

    #for autocomplete
    content_auto = indexes.EdgeNgramField(use_template=True)

    def get_model(self):
        return Project

    def prepare_tags(self, obj):
        return [tag.name for tag in obj.tags.all()]

    def prepare_location(self, obj):
        # If you're just storing the floats...
        return "%s,%s" % (obj.lon, obj.lat)

    def prepare_link(self, obj):
        return obj.get_absolute_url()

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()