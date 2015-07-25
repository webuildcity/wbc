# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin

from models import *

class ProjectAdmin(admin.ModelAdmin):
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

admin.site.register(Project, ProjectAdmin)
admin.site.register(Address, AddressAdmin)