# -*- coding: utf-8 -*-
from __future__ import print_function

from django.conf import settings
from django.core.management.base import BaseCommand

from django.core.urlresolvers import reverse
from django.utils.timezone import now
from django.db.models import Max

from wbc.events.models import Event
from wbc.notifications.models import Subscriber, Newsletter
from wbc.notifications.lib import send_mail

# temporary fix for Django 1.8
# http://stackoverflow.com/questions/29571606/django-not-able-to-render-context-when-in-shell
from django.utils.translation import activate

class Command(BaseCommand):
    help = u'Schickt die Newsletter-Mail für alle seit gestern eingetragenen Events.'

    def handle(self, *args, **options):

        # temporary fix for Django 1.8
        activate('de')

        # get all publication since the last time a newsletter was send
        last = Newsletter.objects.all().aggregate(Max('send'))
        if last['send__max'] == None:
            # first newsletter ever, send all publications
            events = Event.objects.all()
        else:
            events = Event.objects.filter(created__range=[last['send__max'], now()]).all()

        notifications = {}
        for subscriber in Subscriber.objects.all():
            # gather the subscription for the subscribers
            notifications_items = []
            for entity in subscriber.entities.all():
                for event in events:
                    if entity in event.project.entities.all():
                        notifications_items.append(event)
            for project in subscriber.projects.all():
                print(project)
                for event in events:
                    if project in event.projects_events.all():
                        notifications_items.append(event)
                        print(event)

            # Doubletten ausfiltern
            notifications_items = list(set(notifications_items))
            notifications[subscriber.profile.user.email] = notifications_items

        # get the path for places the unsubscribe from a reverse url lookup
        project_path = reverse('wbc.projects.views.project',args=['0']).rstrip('0/') + '/'
        unsubscribe_path = reverse('wbc.notifications.views.unsubscribe',args=['0']).rstrip('0/') + '/'

        i = 0
        for email in notifications:
            print(notifications[email])
            if len(notifications[email]) >0:
                # Mail abschicken
                if email:
                    print(email) 
                    i += 1
                    send_mail(email, 'notifications/mail/newsletter.html', {
                        'events': notifications[email],
                        'project_link': settings.SITE_URL + project_path,
                        # 'unsubscribe_link': settings.SITE_URL + unsubscribe_path + email
                    })

        # store information about this newsletter in the database
        Newsletter(send=now(),n=i).save()

        # print some output
        print(i, "Mails gesendet.")
