from rest_framework.reverse import reverse

from haystack import indexes
from models import Stakeholder


class StakeholderIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    description = indexes.CharField(model_attr='description')
    active = indexes.BooleanField(model_attr='active', null=True)
    tags = indexes.MultiValueField()
    roles = indexes.MultiValueField()
    type = indexes.CharField()

    content_auto = indexes.NgramField(use_template=True)

    def get_model(self):
        return Stakeholder

    def prepare_tags(self, obj):
        return [tag.name for tag in obj.tags.all()]

    def prepare_type(self, obj):
        return 'stakeholder'

    def prepare_roles(self, obj):
        return [role.role for role in obj.roles.all()]

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()