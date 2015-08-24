# -*- coding: utf-8 -*-
from django.contrib import admin

from models import *

class TagAdmin(admin.ModelAdmin):
    list_display = ('slug','name')
    list_display_links = ('slug','name')
    ordering = ['slug']

admin.site.register(WbcTag, TagAdmin)
