# -*- coding: utf-8 -*-
from django.test import TestCase, Client
from projects.models import *

class BbsTestCase(TestCase):
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

    def test_home(self):
        response = Client().get('/')
        self.assertEqual(response.status_code,200)  

    def test_begriffe(self):
        response = Client().get('/begriffe/')
        self.assertEqual(response.status_code,200)
