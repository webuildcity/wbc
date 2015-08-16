# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('enabled','author_name','author_email','place','created')
    list_display_links = ('enabled','author_name','author_email','place','created')
    ordering = ['-created']

admin.site.register(Comment, CommentAdmin)
