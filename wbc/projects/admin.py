# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin

from photologue.admin import GalleryAdmin as GalleryAdminDefault
from photologue.models import Gallery
from models import *

from simple_history.admin import SimpleHistoryAdmin



class ProjectInline(admin.StackedInline):
    model = Project
    can_delete = False

class GalleryAdmin(GalleryAdminDefault):
    inlines = [ProjectInline]

class ProjectAdmin(SimpleHistoryAdmin):
    # inlines = [GalleryInline]

    list_display = ('id','name','address','active')
    list_display_links = ('id','name','address','active')
    # fields = ['active','address','entities','lat','lon','description','identifier','link','polygon']
    ordering = ['id']
    # change_form_template = 'projects/admin/change_form.html'
    # add_form_template = 'projects/admin/change_form.html'

class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'zipcode','street','streetnumber')
    list_display_links = ('id', 'zipcode','street','streetnumber')
    # fields = ['active','address','entities','lat','lon','description','identifier','link','polygon']
    ordering = ['id']

admin.site.unregister(Gallery)
admin.site.register(Gallery, GalleryAdmin)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Address, AddressAdmin)