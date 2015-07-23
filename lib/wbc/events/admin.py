# -*- coding: utf-8 -*-
from django.contrib import admin

from models import *

class DateAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','begin', 'address')
    list_display_links = ('id', 'title','begin', 'address')
    ordering = ['id']

class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'creator', 'indentifier')
    list_display_links = ('id', 'title', 'creator', 'indentifier')
    ordering = ['id']

admin.site.register(Date, DateAdmin)
admin.site.register(Media, MediaAdmin)
