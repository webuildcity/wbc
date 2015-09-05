# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin

from models import *


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'identifier', 'address', 'active')
    list_display_links = ('id', 'identifier', 'address', 'active')
    fields = ['active', 'address', 'entities', 'lat', 'lon',
              'description', 'identifier', 'link', 'polygon', 'building']
    ordering = ['id']
    change_form_template = 'process/admin/change_form.html'
    add_form_template = 'process/admin/change_form.html'


class PublicationAdminForm(forms.ModelForm):

    class Meta:
        model = Publication
        fields = '__all__'

    def __init__(self, *args, **kwds):
        super(PublicationAdminForm, self).__init__(*args, **kwds)
        self.fields['process_step'].queryset = ProcessStep.objects


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'process_step', 'place', 'end')
    list_display_links = ('id', 'process_step', 'place', 'end')
    ordering = ['id']
    form = PublicationAdminForm


class ProcessStepAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order', 'process_type')
    list_display_links = ('id', 'name', 'order', 'process_type')
    ordering = ['id']


class ProcessTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    ordering = ['id']

admin.site.register(Place, PlaceAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(ProcessStep, ProcessStepAdmin)
admin.site.register(ProcessType, ProcessTypeAdmin)
