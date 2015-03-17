# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Installing Behoerden')
        call_command("loaddata", "./fixtures/behoerden.json")
        self.stdout.write('Installing Bezirke')
        call_command("loaddata", "./fixtures/bezirke.json")
        self.stdout.write('Installing Verfahren')
        call_command("loaddata", "./fixtures/verfahren.json")
        self.stdout.write('Installing Verfahrensschritte')
        call_command("loaddata", "./fixtures/verfahrensschritte.json")
        self.stdout.write('Installing Orte')
        call_command("loaddata", "./fixtures/orte.json")
