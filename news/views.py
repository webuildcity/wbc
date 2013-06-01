from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.shortcuts import render,redirect

from news.forms import AbonierenForm, AbbestellenForm
from news.models import Validierung,Abonent,Mail
from projekte.models import Bezirk

import json

def abonieren(request):
    bezirke = Bezirk.objects.all().values()

    if request.method == 'POST':
        form = AbonierenForm(request.POST, bezirke=bezirke)
        if form.is_valid():
            email = form.cleaned_data.pop('email')
            bezirkeJson = json.dumps(form.cleaned_data)
            
            try:
                v = Validierung.objects.get(email=email)
            except Validierung.DoesNotExist:
                v = Validierung(email=email)

            v.bezirke = bezirkeJson
            v.aktion = 'abonieren'
            v.save()

            Mail().abonieren(email, v.code)

            return render(request,'news/abonieren.html', {
                'success': True,
                'abbestellen': settings.SITE_URL + '/news/abbestellen/' + email
            })
    else:
        form = AbonierenForm(bezirke=bezirke)

    return render(request,'news/abonieren.html', {'form': form})

def abbestellen(request, email=None):
    if request.method == 'POST':
        form = AbbestellenForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.pop('email')            
            try:
                abonent = Abonent.objects.get(email=email)

                try:
                    v = Validierung.objects.get(email=email)
                except Validierung.DoesNotExist:
                    v = Validierung(email=email)

                v.aktion='abbestellen'
                v.save()

                Mail().abbestellen(email, v.code)

            except Abonent.DoesNotExist:
                pass # don't tell the user

            return render(request,'news/abbestellen.html', {'success': True})
    else:
        form = AbbestellenForm(initial={'email': email})

    return render(request,'news/abbestellen.html', {'form': form})

def validieren(request, code):
    try:
        validierung = Validierung.objects.get(code=code)
        
        if validierung.aktion == 'abonieren':
            try:
                abonent = Abonent.objects.get(email=validierung.email)
                abonent.bezirke.clear()
            except Abonent.DoesNotExist:
                abonent = Abonent(email=validierung.email)
                abonent.save()

            bezirke = json.loads(validierung.bezirke)
            for key in json.loads(validierung.bezirke):
                if bezirke[key]:
                    abonent.bezirke.add(Bezirk.objects.get(pk=key))
            abonent.save()

            validierung.delete()

        elif validierung.aktion == 'abbestellen':
            try:
                abonent = Abonent.objects.get(email=validierung.email)
                abonent.delete()
            except Abonent.DoesNotExist:
                pass # don't tell the user
                
            validierung.delete()

        else:
            raise Exception('Unbekannte Aktion in `mails_validieren`')

        return render(request,'news/validieren.html', {
            'success': True,
            'aktion': validierung.aktion,
            'abbestellen': settings.SITE_URL + '/news/abbestellen/'
        })
        
    except Validierung.DoesNotExist:
        return render(request,'news/validieren.html', {})
        