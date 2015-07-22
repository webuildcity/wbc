# -*- coding: utf-8 -*-
from django.contrib import admin

from models import *

class TagAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description', 'other')
    list_display_links = ('id','name', 'description')
    ordering = ['id']

admin.site.register(Tag, TagAdmin)
