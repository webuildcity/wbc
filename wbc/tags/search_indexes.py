import datetime
from haystack import indexes
from models import WbcTag


class WbcTagIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')

    #for autocomplete
    content_auto = indexes.EdgeNgramField(use_template=True)

    def get_model(self):
        return WbcTag

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()