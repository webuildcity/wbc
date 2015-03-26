# -*- coding: utf-8 -*-
from django.contrib import admin

from models import Subscriber

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email','created')
    list_display_links = ('email','created')
    ordering = ['id']

admin.site.register(Subscriber, SubscriberAdmin)
