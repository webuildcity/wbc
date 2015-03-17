# -*- coding: utf-8 -*-
from django.contrib import admin

from wbc.news.models import Abonnent

class AbonnentAdmin(admin.ModelAdmin):
    list_display = ('email','created')
    list_display_links = ('email','created')
    ordering = ['id']

admin.site.register(Abonnent, AbonnentAdmin)
