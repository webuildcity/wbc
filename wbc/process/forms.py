# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm

from .models import Place,Publication

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
