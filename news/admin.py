# -*- coding: utf-8 -*-
from django.contrib import admin
from news.models import Abonnent

class AbonnentAdmin(admin.ModelAdmin):
    list_display = ('id','email')
    list_display_links = ('id','email')
    ordering = ['id']

admin.site.register(Abonnent, AbonnentAdmin)
