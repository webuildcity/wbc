from django.contrib import admin
from projekte.models import Projekt, Veroeffentlichung, Verfahrensschritt, Verfahren, Behoerde, Bezirk

admin.site.register(Projekt)
admin.site.register(Veroeffentlichung)
admin.site.register(Verfahrensschritt)
admin.site.register(Verfahren)
admin.site.register(Behoerde)
admin.site.register(Bezirk)