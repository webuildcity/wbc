# -*- coding: utf-8 -*-
import os

from django.conf import settings as django_settings
from django.core.management.base import BaseCommand
from django.core.management import call_command

fixtures = [
    'region/muncipalities.json',
    'region/districts.json',
    'region/departments.json'

    # 'Verfahren',
    # 'Verfahrensschritte',
    # 'Orte',
    # 'Veroeffentlichungen',
    # 'Kommentare'
]

class Command(BaseCommand):

    def handle(self, *args, **options):

        fixture_dir = os.path.join(django_settings.SITE_ROOT,'fixtures')

        for fixture in fixtures:
            self.stdout.write('Installing ' + fixture)
            call_command("loaddata", os.path.join(fixture_dir,fixture))
