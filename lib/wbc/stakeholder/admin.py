# -*- coding: utf-8 -*-
from django.contrib import admin

from models import *

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'address')
    list_display_links = ('id','name', 'address')
    ordering = ['id']

class PersonAdmin(admin.ModelAdmin):
    list_display = ('id','firstName', 'lastName', 'address')
    list_display_links = ('id', 'firstName', 'lastName', 'address')
    ordering = ['id']

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Person, PersonAdmin)
