# -*- coding: utf-8 -*-
from django.contrib import admin

from models import *
from guardian.admin import GuardedModelAdmin

class StakeholderAdmin(GuardedModelAdmin):
    list_display = ('id','name', 'address')
    list_display_links = ('id','name', 'address')
    ordering = ['id']

class StakeholderRoleAdmin(admin.ModelAdmin):
    list_display = ('id','role', 'description')
    list_display_links = ('id','role', 'description')
    ordering = ['id']


class DepartmentAdmin(GuardedModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    ordering = ['id']

admin.site.register(Stakeholder, StakeholderAdmin)
admin.site.register(StakeholderRole, StakeholderRoleAdmin)
admin.site.register(Department, DepartmentAdmin)
