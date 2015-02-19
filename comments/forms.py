from django.forms import ModelForm
from .models import Kommentar

class KommentarForm(ModelForm):

    class Meta:
        model = Kommentar
        fields = ('author_name', 'author_email', 'author_url', 'content')
