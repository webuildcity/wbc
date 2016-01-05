# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin

from .models import *

class ProcessStepAdmin(admin.ModelAdmin):
    list_display = ('id','order','name','process_type','parent_step')
    list_display_links = ('id','order','name','process_type','parent_step')
    ordering = ['id']

class ProcessTypeAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    ordering = ['id']

class ParticipationTypeAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'participation')
    list_display_links = ('id','name', 'participation')
    ordering = ['id']

admin.site.register(ProcessStep, ProcessStepAdmin)
admin.site.register(ProcessType, ProcessTypeAdmin)
admin.site.register(ParticipationType, ParticipationTypeAdmin)
