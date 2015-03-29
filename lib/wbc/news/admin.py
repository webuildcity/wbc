# -*- coding: utf-8 -*-
from django.contrib import admin

from models import Subscriber,Newsletter

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email','created')
    list_display_links = ('email','created')
    ordering = ['id']

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('send','n')
    list_display_links = ('send','n')
    ordering = ['id']

admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Newsletter, NewsletterAdmin)