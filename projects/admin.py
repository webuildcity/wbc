from django.contrib import admin
from projects.models import Project, BBP, Bezirk, Typ

admin.site.register(Project)
admin.site.register(BBP)
admin.site.register(Bezirk)
admin.site.register(Typ)