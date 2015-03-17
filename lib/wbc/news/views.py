# -*- coding: utf-8 -*-
import json

from django.conf import settings
from django.shortcuts import get_object_or_404
from django.shortcuts import render,redirect

from wbc.news.forms import AbonnierenForm, AbbestellenForm
from wbc.news.models import Validierung,Abonnent,Mail
from wbc.projects.models import Bezirk

def abonnieren(request):
    bezirke = Bezirk.objects.all().values()

    if request.method == 'POST':
        form = AbonnierenForm(request.POST, bezirke=bezirke)
        if form.is_valid():
            email = form.cleaned_data.pop('email')
            bezirkeJson = json.dumps(form.cleaned_data)

            try:
                v = Validierung.objects.get(email=email)
            except Validierung.DoesNotExist:
                v = Validierung(email=email)

            v.bezirke = bezirkeJson
            v.aktion = 'abonnieren'
            v.save()

            Mail().abonnieren(email, v.code)

            return render(request,'news/abonnieren.html', {
                'success': True,
                'abbestellen': settings.SITE_URL + '/news/abbestellen/' + email
            })
    else:
        form = AbonnierenForm(bezirke=bezirke)

    return render(request,'news/abonnieren.html', {
        'form': form,
        'abbestellen': settings.SITE_URL + '/news/abbestellen/',
        'bezirke': bezirke
        })

def abbestellen(request, email=None):
    if request.method == 'POST':
        form = AbbestellenForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.pop('email')
            try:
                abonnent = Abonnent.objects.get(email=email)

                try:
                    v = Validierung.objects.get(email=email)
                except Validierung.DoesNotExist:
                    v = Validierung(email=email)

                v.aktion='abbestellen'
                v.save()

                Mail().abbestellen(email, v.code)

            except Abonnent.DoesNotExist:
                pass # don't tell the user

            return render(request,'news/abbestellen.html', {'success': True})
    else:
        form = AbbestellenForm(initial={'email': email})

    return render(request,'news/abbestellen.html', {'form': form})

def validieren(request, code):
    try:
        validierung = Validierung.objects.get(code=code)

        if validierung.aktion == 'abonnieren':
            try:
                abonnent = Abonnent.objects.get(email=validierung.email)
                abonnent.bezirke.clear()
            except Abonnent.DoesNotExist:
                abonnent = Abonnent(email=validierung.email)
                abonnent.save()

            bezirke = json.loads(validierung.bezirke)
            for key in json.loads(validierung.bezirke):
                if bezirke[key]:
                    abonnent.bezirke.add(Bezirk.objects.get(pk=key))
            abonnent.save()

            validierung.delete()

        elif validierung.aktion == 'abbestellen':
            try:
                abonnent = Abonnent.objects.get(email=validierung.email)
                abonnent.delete()
            except Abonnent.DoesNotExist:
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
