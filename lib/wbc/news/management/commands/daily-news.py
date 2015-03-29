# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.management.base import BaseCommand

from django.core.urlresolvers import reverse
from django.utils.timezone import now
from django.db.models import Max

from wbc.process.models import Publication
from wbc.news.models import Subscriber, Newsletter
from wbc.news.lib import send_mail

class Command(BaseCommand):
    help = u'Schickt die Newsletter-Mail für alle seit gestern eingetragenen Veröffentlichungen.'

    def handle(self, *args, **options):
        # get all publication since the last time a newsletter was send
        last = Newsletter.objects.all().aggregate(Max('send'))
        if last['send__max'] == None:
            # first newsletter ever, send all publications
            publications = Publication.objects.all()
        else:
            publications = Publication.objects.filter(created__range=[last['send__max'], now()]).all()

        news = {}
        for subscriber in Subscriber.objects.all():
            # gather the subscription for the subscribers
            news_items = []
            for entity in subscriber.entities.all():
                for publication in publications:
                    if entity in publication.place.entities.all():
                        news_items.append(publication)

            # Doubletten ausfiltern
            news_items = list(set(news_items))

            # an zu verschickende News anhängen
            news[subscriber.email] = news_items

        # get the link for places the unsubscribe from a reverse url lookup
        place_link = reverse('wbc.process.views.place',args=['.']).strip('.')
        unsubscribe_link = reverse('wbc.news.views.unsubscribe',args=['.']).strip('.')

        i = 0
        for email in news:
            # Mail abschicken
            if news[email]:
                i += 1

                send_mail(email, 'news/mail/newsletter.html', {
                    'publications': news[email],
                    'place_link': settings.SITE_URL + place_link,
                    'unsubscribe_link': settings.SITE_URL + unsubscribe_link + email
                })

        # store information about this newsletter in the database
        # Newsletter(send=now(),n=i).save()

        # print some output
        print i,"Mails gesendet."
