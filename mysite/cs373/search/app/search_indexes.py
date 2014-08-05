from haystack import indexes
from myapp.models import Note

#describes from what fields things are pulled
class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.NgramField(document=True, use_template=True)
    #search by note author, pub date, title, and body --used by .txt template
    author = indexes.CharField(model_attr='user')
    pub_date = indexes.DateTimeField(model_attr='pub_date')
    title = indexes.CharField(model_attr='title')
    body = indexes.CharField(model_attr='body')
    content_auto=indexes.EdgeNgramField(model_attr='title')


    def get_model(self):
        return Note

    #used when building on the command line
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

