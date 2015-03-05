# -*- coding: utf-8 -*-
import sys,os,datetime
from django.utils.timezone import now
from django.core.management.base import BaseCommand, CommandError

from projects.models import Bezirk,Ort,Veroeffentlichung
from news.models import Abonnent,Mail

class Command(BaseCommand):
    help = u'Schickt die newsletter mail für all seid gestern eingetragenen Veröffentlichungen.'

    def handle(self, *args, **options):
        # gegenwärtige Zeit finden
        yesterday = now() - datetime.timedelta(days=1)

        # neue Veröffentlichungen finden
        veroeffentlichungen = Veroeffentlichung.objects.filter(created__range=[yesterday, now()]).all()

        news = {}
        for abonnent in Abonnent.objects.all():
            # die Veroeffentlichungen fuer den Abonenten sammeln
            n = []
            for bezirk in abonnent.bezirke.all():
                for veroeffentlichung in veroeffentlichungen:
                    if bezirk in veroeffentlichung.ort.bezirke.all():
                        n.append(veroeffentlichung)

            # Doubletten ausfiltern
            n = list(set(n))

            # an zu verschickende News anhängen
            news[abonnent.email] = n

        i = 0
        for email in news:
            # Mail abschicken
            if news[email]:
                i+=1
                Mail().newsletter(email,news[email])

        print i,"Mails gesendet."
