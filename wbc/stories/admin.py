# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *
from guardian.admin import GuardedModelAdmin


class StoryAdmin(GuardedModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    ordering = ['id']

class BaseStepAdmin(GuardedModelAdmin):
    list_display = ('identifier','name')
    list_display_links = ('identifier','name')
    ordering = ['identifier']

class AnchorAdmin(GuardedModelAdmin):
    list_display = ('identifier','name')
    list_display_links = ('identifier','name')
    ordering = ['identifier']

class SubstepAdmin(GuardedModelAdmin):
    list_display = ('identifier','name')
    list_display_links = ('identifier','name')
    ordering = ['identifier']

admin.site.register(Story, StoryAdmin)
admin.site.register(BaseStep, BaseStepAdmin)
admin.site.register(Anchor, AnchorAdmin)
admin.site.register(Substep, SubstepAdmin)
