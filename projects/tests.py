# -*- coding: utf-8 -*-
from django.test import TestCase
from projects.models import Ort, Veroeffentlichung, Verfahrensschritt, Verfahren, Behoerde, Bezirk

class ProjectsTestCase(TestCase):
    def test_bezirke(self):
        a = Bezirk.objects.get(name='Mitte')
        b = Bezirk.objects.all()
        self.assertIn(a,b)

    def test_behoerde(self):
        a = Behoerde.objects.get(name='Bezirksamt Mitte')
        b = Behoerde.objects.all()
        self.assertIn(a,b)

    def test_verfahrensschritt(self):
        a = Verfahrensschritt.objects.get(name='Frühzeitige Öffentlichkeitsbeteiligung')
        b = Verfahrensschritt.objects.all()
        self.assertIn(a,b)

    def test_verfahren(self):
        a = Verfahren.objects.get(name='Bebauungsplanverfahren')
        b = Verfahren.objects.all()
        self.assertIn(a,b)

    def test_ort(self):
        # store ne project
        a = Ort(adresse='Unter den Linden 1',beschreibung='Brandenburger Tor',lat='-13',lon='52',bezeichner='ACB')
        a.save()
        b = Bezirk.objects.get(name='Mitte')
        a.bezirke.add(b)
        a.save()

        # retrieve project
        c = Ort.objects.get(bezeichner='ACB')
        self.assertIn(b,c.bezirke.all())

    def test_veroeffentlichung(self):
        pass