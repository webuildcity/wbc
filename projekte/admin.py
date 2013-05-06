from django.contrib import admin
from projekte.models import Projekt, Veroeffentlichung, Verfahrensschritt, Verfahren, Behoerde, Bezirk

class ProjektAdmin(admin.ModelAdmin):
    list_display = ('id','bezeichner','adresse')
    ordering = ['id']

class VeroeffentlichungAdmin(admin.ModelAdmin):
    list_display = ('id','verfahrensschritt','projekt','ende')
    ordering = ['id']

class VerfahrensschrittAdmin(admin.ModelAdmin):
    list_display = ('id','name','reihenfolge','verfahren')
    ordering = ['id']

class VerfahrenAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    ordering = ['id']

class BehoerdeAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    ordering = ['id']

class BezirkAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    ordering = ['id']

admin.site.register(Projekt, ProjektAdmin)
admin.site.register(Veroeffentlichung, VeroeffentlichungAdmin)
admin.site.register(Verfahrensschritt, VerfahrensschrittAdmin)
admin.site.register(Verfahren, VerfahrenAdmin)
admin.site.register(Behoerde, BehoerdeAdmin)
admin.site.register(Bezirk, BezirkAdmin)