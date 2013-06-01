from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render,redirect
from mails.forms import AbonierenForm, AbbestellenForm

from projekte.models import Bezirk
from mails.models import Validierung,Abonent

import json

def abonieren(request):
    bezirke = Bezirk.objects.all().values()

    if request.method == 'POST':
        form = AbonierenForm(request.POST, bezirke=bezirke)
        if form.is_valid():
            e = form.cleaned_data.pop('email')
            b = json.dumps(form.cleaned_data)
            
            v = Validierung(email=e,bezirke=b,aktion='abonieren')
            v.save()

            return render(request,'mails/abonieren.html', {'success': True})
    else:
        form = AbonierenForm(bezirke=bezirke)

    return render(request,'mails/abonieren.html', {'form': form})

def validieren(request, code):
    try:
        validierung = Validierung.objects.get(code=code)
        
        if validierung.aktion == 'abonieren':
            abonent = Abonent(email=validierung.email)
            abonent.save()

            bezirke = json.loads(validierung.bezirke)
            for key in json.loads(validierung.bezirke):
                if bezirke[key]:
                    abonent.bezirke.add(Bezirk.objects.get(pk=key))

            abonent.save()

            validierung.delete()

        elif validierung.aktion == 'abbestellen':
            abonent = Abonent.objects.get(email=validierung.email)
            abonent.delete()
            
            validierung.delete()

        else:
            raise Exception('Unbekannte Aktion in `mails_validieren`')

        return render(request,'mails/validieren.html', {'success': True, 'aktion': validierung.aktion})
    except Validierung.DoesNotExist:
        return render(request,'mails/validieren.html', {})
        
def abbestellen(request, email=None):
    if request.method == 'POST':
        form = AbbestellenForm(request.POST)
        if form.is_valid():
            e = form.cleaned_data.pop('email')            
            try:
                abonent = Abonent.objects.get(email=e)

                v = Validierung(email=e,bezirke=None,aktion='abbestellen')
                v.save()
            except Abonent.DoesNotExist:
                pass # don't tell the user

            return render(request,'mails/abbestellen.html', {'success': True})
    else:
        form = AbbestellenForm(initial={'email': email})

    return render(request,'mails/abbestellen.html', {'form': form})
