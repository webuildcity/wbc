# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client
from models import Validation
from models import Subscriber
from models import Newsletter
from wbc.region.models import Entity
from models import *
from forms import SubscribeForm
from django.test.client import RequestFactory
from django.utils.timezone import now

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
        self.entity = Entity(name='Berlin').save()
        self.entity2 = Entity(name='Hamburg').save()
        self.factory = RequestFactory()
        self.entities = Entity.objects.all().values()
        self.validation = Validation(email='test@test.de')

    # Models

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

    # Form

    def test_subscribe_form(self):
        data = {'email': 'test@test.de'}
        request = self.factory.post('', data)
        form = SubscribeForm(request.POST, entities=self.entities)
        self.assertTrue(isinstance(form, SubscribeForm))

    # Views

    def test_subscribe_view(self):
        url = reverse('wbc.news.views.subscribe')
        resp = Client().post(url, {'username': self.user.username})


class NewsletterTestCase(TestCase):

    def create_newsletter(email='test@test.de'):
        n = Newsletter.objects.create(send=now(), n=5)
        return n

    def test_validation(self):
        n = self.create_newsletter()
        self.assertTrue(isinstance(n, Newsletter))
        time_string = n.send.strftime("%d. %m. %Y, %H:%M:%S")
        self.assertEqual(
            n.__unicode__(), time_string)
