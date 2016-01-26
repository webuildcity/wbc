# -*- coding: utf-8 -*-
from django.contrib import admin

from models import *
from guardian.admin import GuardedModelAdmin

class EventAdmin(GuardedModelAdmin):
    list_display = ('id', 'title','begin')
    list_display_links = ('id', 'title','begin')
    ordering = ['id']

class DateAdmin(GuardedModelAdmin):
    list_display = ('id', 'title','begin', 'address')
    list_display_links = ('id', 'title','begin', 'address')
    ordering = ['id']

class MediaAdmin(GuardedModelAdmin):
    list_display = ('id', 'title', 'creator', 'indentifier')
    list_display_links = ('id', 'title', 'creator', 'indentifier')
    ordering = ['id']

class PublicationAdmin(GuardedModelAdmin):
    list_display = ('id', 'project', 'begin')
    list_display_links = ('id', 'project', 'begin')
    ordering = ['id']

#admin.site.register(Event, EventAdmin)
admin.site.register(Date, DateAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Publication, PublicationAdmin)
