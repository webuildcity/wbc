# -*- coding: utf-8 -*-
from django.test import TestCase, Client
from projects.models import *

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

    def test_bezirke(self):
        a = Bezirk.objects.get(pk=1)
        b = Bezirk.objects.all()
        self.assertIn(a,b)

    def test_behoerde(self):
        a = Behoerde.objects.get(pk=1)
        b = Behoerde.objects.all()
        self.assertIn(a,b)

    def test_verfahrensschritt(self):
        a = Verfahrensschritt.objects.get(pk=1)
        b = Verfahrensschritt.objects.all()
        self.assertIn(a,b)

    def test_verfahren(self):
        a = Verfahren.objects.get(pk=1)
        b = Verfahren.objects.all()
        self.assertIn(a,b)

    def test_ort(self):
        a = Ort.objects.get(pk=1)
        b = Ort.objects.all()
        self.assertIn(a,b)

        response = Client().get('/orte/')
        self.assertEqual(response.status_code,200)

        response = Client().get('/orte/1/')
        self.assertEqual(response.status_code,200)

    def test_veroeffentlichung(self):
        a = Veroeffentlichung.objects.get(pk=1)
        b = Veroeffentlichung.objects.all()
        self.assertIn(a,b)