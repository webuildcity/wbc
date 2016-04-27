from django import forms
from django.contrib import admin

from models import *

from simple_history.admin import SimpleHistoryAdmin
from guardian.admin import GuardedModelAdmin

class PhotoAdmin(GuardedModelAdmin, SimpleHistoryAdmin):
    list_display = ('id', 'file')
    list_display_links = ('id', 'file')
    ordering = ['id']

class AlbumAdmin(GuardedModelAdmin, SimpleHistoryAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    ordering = ['id']

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Album, AlbumAdmin)