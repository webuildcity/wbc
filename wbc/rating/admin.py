from django.contrib import admin

from models import *


class WbcRatingAdmin(admin.ModelAdmin):
    list_display = ('id','user','project','tag')
    list_display_links = ('id','user','project','tag')
    ordering = ['id']

admin.site.register(WbcRating, WbcRatingAdmin)
