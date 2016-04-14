# coding: utf-8
import os,sys,importlib

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = u'links ausgleichsflächen to projects.'

    def handle(self, *args, **options):
        project_name = settings.ROOT_URLCONF.replace('.urls','')

        try:
            fetch = importlib.import_module(project_name + '.fetch')
        except ImportError:
            sys.exit('Error: ' + os.path.join(settings.SITE_ROOT,project_name,'fetch.py') + ' does not exist.')

        try:
            p = fetch.ProjectAfLink()
        except AttributeError:
            sys.exit('Error: fetch.ProjectAfLink does not exist.')

        p.fetch()