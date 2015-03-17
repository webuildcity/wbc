# -*- coding: utf-8 -*-
from django.test import TestCase, Client

from wbc.projects.models import *
from wbc.news.models import *

class NewsTestCase(TestCase):
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

    def test_news(self):
        client = Client()

        # get the abonnieren page
        response = client.get('/news/abonnieren/')
        self.assertEqual(response.status_code,200)

        # send the form 
        response = client.post('/news/abonnieren/', {
            'email': 'example@example.com',
            '1': 'on',
            '2': 'on'
        })
        self.assertEqual(response.status_code,200)

        # check if the user is in the database
        v = Validierung.objects.get(email='example@example.com')
        self.assertEqual(v.aktion,'abonnieren')

        # validate the user
        response = client.get('/news/validieren/' + v.code)
        self.assertEqual(response.status_code,200)

        # get the abbestellen page
        response = client.get('/news/abbestellen/')
        self.assertEqual(response.status_code,200)

        # get it with email
        response = client.get('/news/abbestellen/' + v.email)
        self.assertEqual(response.status_code,200)

        # cancel the subscription
        response = client.post('/news/abbestellen/', {
            'email': 'example@example.com',
        })
        self.assertEqual(response.status_code,200)

        # check if the user is in the database
        v = Validierung.objects.get(email='example@example.com')
        self.assertEqual(v.aktion,'abbestellen')

        # validate the user
        response = client.get('/news/validieren/' + v.code)
        self.assertEqual(response.status_code,200)
