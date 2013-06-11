from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.serializers.json import DjangoJSONEncoder
import json

from bbs.lib import RestView
from projekte.models import Projekt, Veroeffentlichung, Verfahrensschritt, Verfahren, Behoerde, Bezirk

#class ProjekteView():

def get_items(request):
    projekte = Projekt.objects.all()
    response = {'projekte': projekte}
    return render(request,'projekte/projekte.html', response)

def get_item(request, pk):
    projekt = Projekt.objects.get(pk=int(pk))
    response = {'projekt': projekt}
    return render(request,'projekte/projekt.html', response)

#    # this function overides the corresponding function in RestView
#    def jsonResponse(self, jsonObject):
#        return HttpResponse(json.dumps(jsonObject, cls=DjangoJSONEncoder), content_type="application/json")

class VeroeffentlichungenView(RestView):

    def get_items(self, request):
        veroeffentlichungen = Veroeffentlichung.objects.all()
        response = {'veroeffentlichungen': veroeffentlichungen}
        return self.render(request,'projekte/veroeffentlichungen.html', response)

    def get_item(self, request, pk):
        veroeffentlichung = Veroeffentlichung.objects.get(pk=int(pk))
        response = {'veroeffentlichung': veroeffentlichung}
        return self.render(request,'projekte/veroeffentlichung.html', response)

    # this function overides the corresponding function in RestView
    def jsonResponse(self, jsonObject):
        return HttpResponse(json.dumps(jsonObject, cls=DjangoJSONEncoder), content_type="application/json")
