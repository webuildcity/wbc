# -*- coding: utf-8 -*-
from django.contrib import admin

from wbc.comments.models import Kommentar

class KommentarAdmin(admin.ModelAdmin):
    list_display = ('enabled','author_name','author_email','ort','created')
    list_display_links = ('enabled','author_name','author_email','ort','created')
    ordering = ['-created']

admin.site.register(Kommentar, KommentarAdmin)