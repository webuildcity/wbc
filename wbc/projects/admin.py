# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin

from models import *

from simple_history.admin import SimpleHistoryAdmin
from guardian.admin import GuardedModelAdmin


class ProjectInline(admin.StackedInline):
    model = Project
    can_delete = False

# class GalleryAdmin(GalleryAdminDefault):
#     inlines = [ProjectInline]

class ProjectAdmin(GuardedModelAdmin, SimpleHistoryAdmin):
    # inlines = [GalleryInline]

    list_display = ('id','name','address','active')
    list_display_links = ('id','name','address','active')
    # fields = ['active','address','entities','lat','lon','description','identifier','link','polygon']
    ordering = ['id']
    # change_form_template = 'projects/admin/change_form.html'
    # add_form_template = 'projects/admin/change_form.html'

class BufferAreaAdmin(GuardedModelAdmin, SimpleHistoryAdmin):
    # inlines = [GalleryInline]

    list_display = ('id','name', 'identifier', 'active')
    list_display_links = ('id','name', 'identifier', 'active')
    # fields = ['active','address','entities','lat','lon','description','identifier','link','polygon']
    ordering = ['id']
    # change_form_template = 'projects/admin/change_form.html'
    # add_form_template = 'projects/admin/change_form.html'

class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'zipcode','street','streetnumber')
    list_display_links = ('id', 'zipcode','street','streetnumber')
    # fields = ['active','address','entities','lat','lon','description','identifier','link','polygon']
    ordering = ['id']

# admin.site.unregister(Gallery)
# admin.site.register(Gallery, GalleryAdmin)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(BufferArea, BufferAreaAdmin)
