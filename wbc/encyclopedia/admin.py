# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin

from .models import *

class EncyclopediaEntryAdmin(admin.ModelAdmin):
    list_display = ('id','order','title','parent_entry')
    list_display_links = ('id','order','title','parent_entry')
    ordering = ['id']

admin.site.register(EncyclopediaEntry, EncyclopediaEntryAdmin)
