# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.contrib.contenttypes.models import ContentType
from django.forms import widgets

from models import Place
from models import Publication
from models import ProcessStep


class FindPlace(forms.Form):
    place = Place.objects.all()
    description = forms.CharField(max_length=100, required=False)


class CreatePublication(ModelForm):
    class Meta:
        model = Publication
        fields = '__all__'


class CreatePlace(ModelForm):
    class Meta:
        model = Place
        exclude = ('polygontype',)


class ProcessstepForm(ModelForm):
    class Meta:
        #CHOICES = ContentType.objects.all().filter(app_label='participation')
        #choices = list((x.model, x.name) for x in CHOICES)
        choices = []
        choices.insert(0, ("", "--------------"))
        model = ProcessStep
        fields = '__all__'
        widgets = {
            'participation': widgets.Select(choices=choices)
        }
