import datetime
from haystack import indexes
from cs373.models import *


class ArtistIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.NgramField(document=True, use_template=True)

    def get_model(self):
        return Artist

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


class SponsorIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.NgramField(document=True, use_template=True)

    def get_model(self):
        return Sponsor

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

class StageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.NgramField(document=True, use_template=True)

    def get_model(self):
        return StageMedia

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()