# -*- coding: utf-8 -*-
from django.contrib import admin

from models import *

class BlogEntryAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')
    ordering = ['id']

admin.site.register(BlogEntry, BlogEntryAdmin)
