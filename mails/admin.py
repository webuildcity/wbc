from django.contrib import admin
from mails.models import Abonent

class AbonentAdmin(admin.ModelAdmin):
    list_display = ('id','email')
    list_display_links = ('id','email')
    ordering = ['id']

admin.site.register(Abonent, AbonentAdmin)
