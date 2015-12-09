# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin

from .models import *

class ProcessStepAdmin(admin.ModelAdmin):
    list_display = ('id','name','order','process_type')
    list_display_links = ('id','name','order','process_type')
    ordering = ['id']

class ProcessTypeAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    ordering = ['id']

class ParticipationFormAdmin(admin.ModelAdmin):
    list_display = ('id','name','participation')
    list_display_links = ('id','name','participation')
    ordering = ['id']

class ArticleTypeAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    ordering = ['id']

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'article_type', 'created_at', 'modified_at')
    list_display_links = ('id','title')
    ordering = ['id']

admin.site.register(ProcessStep, ProcessStepAdmin)
admin.site.register(ProcessType, ProcessTypeAdmin)
admin.site.register(ParticipationForm, ParticipationFormAdmin)
admin.site.register(ArticleType, ArticleTypeAdmin)
admin.site.register(Article, ArticleAdmin)
