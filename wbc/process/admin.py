# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin

from .models import *

class ProcessStepAdmin(admin.ModelAdmin):
    list_display = ('id','name','order','process_type')
    list_display_links = ('id','name','order','process_type')
    ordering = ['id']

class ProcessTypeAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    ordering = ['id']

admin.site.register(ProcessStep, ProcessStepAdmin)
admin.site.register(ProcessType, ProcessTypeAdmin)
