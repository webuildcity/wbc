# -*- coding: utf-8 -*-
import os

from django.conf import settings as django_settings
from django.core.management.base import BaseCommand
from django.core.management import call_command

fixtures = [
    # region
    'region/muncipalities.json',
    'region/districts.json',
    'region/quarters.json',
    # process
    'process/processtypes.json',
    'process/processsteps.json',
    # projects
    'projects/project.json'
    # comments
    'comments/comments.json',
    # news
    'notifications/subscriber.json',
    #stakeholder
    'stakeholder/departments.json',
    #photologue
    'photologue/photosize.json',
]

class Command(BaseCommand):

    def handle(self, *args, **options):

        fixture_dir = os.path.join(django_settings.SITE_ROOT,'fixtures')

        for fixture in fixtures:
            filepath = os.path.join(fixture_dir,fixture)

            if os.path.isfile(filepath):
                self.stdout.write('Installing ' + fixture)
                call_command("loaddata", filepath)
