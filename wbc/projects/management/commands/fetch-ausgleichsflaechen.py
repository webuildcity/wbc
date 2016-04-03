#!/usr/bin/env python
# coding: utf-8
import os,sys,importlib

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = u'Fetches the information about the ausgleigchsflaechen.'

    def handle(self, *args, **options):
        project_name = settings.ROOT_URLCONF.replace('.urls','')

        try:
            fetch = importlib.import_module(project_name + '.fetch')
        except ImportError:
            sys.exit('Error: ' + os.path.join(settings.SITE_ROOT,project_name,'fetch.py') + ' does not exist.')

        try:
            p = fetch.AusgleichsflaechenFetcher()
        except AttributeError:
            sys.exit('Error: fetch.AusgleichsflaechenFetcher does not exist.')

        p.fetch()
