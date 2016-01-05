from django import forms
from models import *

from django_markdown.widgets import MarkdownWidget


class BlogEntryForm(forms.ModelForm):
    class Meta:
        model = BlogEntry
        fields = '__all__'

    # content = forms.CharField(widget=MarkdownWidget())

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)

    def save(self):
        instance = forms.ModelForm.save(self)
        return instance