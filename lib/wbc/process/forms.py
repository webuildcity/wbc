# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.contrib.contenttypes.models import ContentType
from django.forms import widgets

from models import Place
from models import Publication
from models import ProcessStep


class ParticipationSelect(widgets.Select):

    def __init__(self, *args, **kwargs):
        super(ParticipationSelect, self).__init__(*args, **kwargs)

        participation_models = ContentType.objects.all().filter(app_label='participation')

        self.choices = [('', '---------')]
        self.choices += list((x.model, x.name) for x in participation_models)


class ProcessstepForm(ModelForm):
    class Meta:
        model = ProcessStep
        fields = '__all__'
        widgets = {
            'participation': ParticipationSelect()
        }
