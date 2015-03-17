# -*- coding: utf-8 -*-
from django.test import TestCase, Client

from wbc.projects.models import *

class ProjectsTestCase(TestCase):
    def setUp(self):
        a = Ort(
            adresse='Unter den Linden 1',
            beschreibung='Brandenburger Tor',
            lat='-13',
            lon='52',
            bezeichner='ACB'
        )
        a.save()
        b = Bezirk.objects.get(name='Mitte')
        a.bezirke.add(b)
        a.save()

        c = Veroeffentlichung(
            verfahrensschritt=Verfahrensschritt.objects.get(pk=1),
            ort=Ort.objects.get(pk=1),
            beginn='2010-10-10',
            ende='2010-11-10',
            behoerde=Behoerde.objects.get(pk=1)
        )
        c.save()

    def test_ort(self):
        client = Client()
        response = client.get('/orte/')
        self.assertEqual(response.status_code,200)

        response = client.get('/orte/1/')
        self.assertEqual(response.status_code,200)
