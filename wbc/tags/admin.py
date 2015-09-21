# -*- coding: utf-8 -*-
from django.contrib import admin

from models import *
from taggit.admin import *

class WbcTagAdmin(admin.ModelAdmin):
    list_display = ('slug','name')
    list_display_links = ('slug','name')
    ordering = ['slug']

# admin.site.unregister(TagAdmin)
admin.site.register(WbcTag, WbcTagAdmin)