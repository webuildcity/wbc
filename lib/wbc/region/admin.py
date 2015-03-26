# -*- coding: utf-8 -*-
from django.contrib import admin

from wbc.region.models import *

class MuncipalityAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    ordering = ['id']

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    ordering = ['id']

class QuarterAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    ordering = ['id']

class OfficeAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    ordering = ['id']

admin.site.register(Muncipality, MuncipalityAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Quarter, QuarterAdmin)
admin.site.register(Office, OfficeAdmin)
