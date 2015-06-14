# -*- coding: utf-8 -*-
from django.test import TestCase
from models import Validation
from models import Subscriber
from models import Newsletter
from wbc.region.models import Entity
from models import *

# Test for Models


class NewsTestCase(TestCase):

    def create_validation(email='test@test.de', code='xyz', action='action'):
        return Validation.objects.create(email=email, code=code, action=action)

    def test_validation(self):
        v = self.create_validation()
        self.assertTrue(isinstance(v, Validation))
        self.assertEqual(
            v.__unicode__(), v.email)


class SubscriberTestCase(TestCase):

    def setUp(self):
        Entity(name='Berlin').save()

    def create_subscriber(email='test@test.de'):
        entity = Entity.objects.get(name='Berlin')
        s = Subscriber.objects.create(email=email)
        s.entities.add(entity)
        return s

    def test_validation(self):
        s = self.create_subscriber()
        self.assertTrue(isinstance(s, Subscriber))
        self.assertEqual(
            s.__unicode__(), s.email)


class NewsletterTestCase(TestCase):

    def create_newsletter(email='test@test.de'):
        import datetime
        now = datetime.datetime.now()
        n = Newsletter.objects.create(send=now, n=5)
        return n

    def test_validation(self):
        n = self.create_newsletter()
        self.assertTrue(isinstance(n, Newsletter))
        time_string = n.send.strftime("%d. %m. %Y, %H:%M:%S")
        self.assertEqual(
            n.__unicode__(), time_string)
