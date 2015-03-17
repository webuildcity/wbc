# -*- coding: utf-8 -*-
from django.forms import ModelForm

from wbc.comments.models import Kommentar

class KommentarForm(ModelForm):

    class Meta:
        model = Kommentar
        fields = ('author_name', 'author_email', 'author_url', 'content')
