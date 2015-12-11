# -*- coding: utf-8 -*-
from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from models import *

class BlogEntryAdmin(SimpleHistoryAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')
    ordering = ['id']

admin.site.register(BlogEntry, BlogEntryAdmin)
