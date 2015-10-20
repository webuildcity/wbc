# -*- coding: utf-8 -*-
from json import loads, dumps

from django.conf import settings
from django.shortcuts import render
from django.core.urlresolvers import reverse

from wbc.region.models import District

from .forms import SubscribeForm, UnsubscribeForm
from .models import Validation, Subscriber
from .lib import send_mail


def subscribe(request):
    entities = District.objects.all().values()

    unsubscribe_path = reverse(
        'wbc.notifications.views.unsubscribe', args=['.']).strip('.')
    validate_path = reverse('wbc.notifications.views.validate', args=['.']).strip('.')

    if request.method == 'POST':
        form = SubscribeForm(request.POST, entities=entities)
        if form.is_valid():
            email = form.cleaned_data.pop('email')
            entitiesJson = dumps(form.cleaned_data)

            try:
                v = Validation.objects.get(email=email)
            except Validation.DoesNotExist:
                v = Validation(email=email)

            v.entities = entitiesJson
            v.action = 'subscribe'
            v.save()

            send_mail(email, 'notifications/mail/subscribe.html', {
                'unsubscribe_link': settings.SITE_URL + unsubscribe_path + email,
                'validate_link': settings.SITE_URL + validate_path + v.code
            })

            return render(request, 'notifications/subscribe.html', {
                'success': True,
                'unsubscribe_link': settings.SITE_URL + unsubscribe_path + email
            })
    else:
        form = SubscribeForm(entities=entities)

    return render(request, 'notifications/subscribe.html', {
        'form': form,
        'unsubscribe_link': settings.SITE_URL + unsubscribe_path,
        'entities': entities
    })


def unsubscribe(request, email=None):
    if request.method == 'POST':
        form = UnsubscribeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.pop('email')
            try:
                subscriber = Subscriber.objects.get(email=email)

                try:
                    v = Validation.objects.get(email=email)
                except Validation.DoesNotExist:
                    v = Validation(email=email)

                v.action = 'unsubscribe'
                v.save()

                validate_path = reverse(
                    'wbc.notifications.views.validate', args=['.']).strip('.')

                send_mail(email, 'notifications/mail/unsubscribe.html', {
                    'validate_link': settings.SITE_URL + validate_path + v.code
                })

            except Subscriber.DoesNotExist:
                pass  # don't tell the user

            return render(request, 'notifications/unsubscribe.html', {'success': True})
    else:
        form = UnsubscribeForm(initial={'email': email})

    return render(request, 'notifications/unsubscribe.html', {'form': form})


def validate(request, code):
    try:
        validation = Validation.objects.get(code=code)

        if validation.action == 'subscribe':
            try:
                subscriber = Subscriber.objects.get(email=validation.email)
                subscriber.entities.clear()
            except Subscriber.DoesNotExist:
                subscriber = Subscriber(email=validation.email)
                subscriber.save()

            entities = loads(validation.entities)
            for key in entities:
                if entities[key]:
                    subscriber.entities.add(District.objects.get(pk=key))
            subscriber.save()

            validation.delete()

        elif validation.action == 'unsubscribe':
            try:
                subscriber = Subscriber.objects.get(email=validation.email)
                subscriber.delete()
            except Subscriber.DoesNotExist:
                pass  # don't tell the user

            validation.delete()

        else:
            raise Exception(
                "Unknown action '%s' for validation" % validation.action)

        unsubscribe_path = reverse(
            'wbc.notifications.views.unsubscribe', args=['.']).strip('.')

        return render(request, 'notifications/validate.html', {
            'success': True,
            'action': validation.action,
            'unsubscribe_link': settings.SITE_URL + unsubscribe_path
        })

    except Validation.DoesNotExist:
        return render(request, 'notifications/validate.html', {})
