# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client
from .models import Validation
from .models import Subscriber
from .models import Newsletter
from wbc.region.models import Entity, Muncipality, District
from .models import *
from .forms import SubscribeForm
from django.test.client import RequestFactory
from django.utils.timezone import now
from django.core.urlresolvers import reverse

# Test for Models


class notificationsTestCase(TestCase):

    def create_validation(email='test@test.de', code='xyz', action='action'):
        return Validation.objects.create(email=email, code=code, action=action)

    def test_validation(self):
        v = self.create_validation()
        self.assertTrue(isinstance(v, Validation))
        self.assertEqual(
            v.__unicode__(), v.email)


class SubscriberTestCase(TestCase):

    def setUp(self):
        self.entity = Entity(name='München').save()
        self.entity2 = Entity(name='Hamburg').save()
        Muncipality(name='Berlin').save()
        self.muncipality = Muncipality.objects.get(name='Berlin')
        District(name="Charlottenburg", muncipality=self.muncipality).save()
        District(name="Schöneberg", muncipality=self.muncipality).save()
        self.factory = RequestFactory()
        self.entities = Entity.objects.all().values()

    # Models

    def create_subscriber(self, email='test@test.de'):
        entity = Entity.objects.get(name='Charlottenburg')
        s = Subscriber.objects.create(email=email)
        s.entities.add(entity)
        s.save()
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

    def test_subscribe_view_post(self):
        url = reverse('wbc.notifications.views.subscribe')
        Client().post(url, {'email': 'test1@test.de'})
        validation = Validation.objects.get(email='test1@test.de')
        self.assertEqual(validation.email, 'test1@test.de')

    def test_subscribe_view_get(self):
        url = reverse('wbc.notifications.views.subscribe')
        page = Client().get(url)
        self.assertEqual(page.status_code, 200)
        self.assertEqual(len(page.context['entities']), 2)

    def test_unsubscribe_view_post(self):
        subscriber = self.create_subscriber()
        count = Subscriber.objects.all().count()
        self.assertEqual(count, 1)
        url = reverse('wbc.notifications.views.unsubscribe', args=[subscriber.email])
        page = Client().post(url, {'email': subscriber.email})
        validation = Validation.objects.get(email=subscriber.email)
        self.assertEqual(validation.action, 'unsubscribe')
        self.assertEqual(page.status_code, 200)
        self.assertEqual(page.context['success'], True)

    def test_unsubscribe_view_post_email_does_not_exist(self):
        email = 'test3@test.de'
        try:
            Subscriber.objects.get(email=email)
        except:
            exists = False
        self.assertEqual(exists, False)
        url = reverse('wbc.notifications.views.unsubscribe', args=[email])
        page = Client().post(url, {'email': email})
        self.assertEqual(page.status_code, 200)
        self.assertEqual(page.context['success'], True)

    def test_unsubscribe_view_get(self):
        subscriber = self.create_subscriber()
        count = Subscriber.objects.all().count()
        self.assertEqual(count, 1)
        url = reverse('wbc.notifications.views.unsubscribe', args=[subscriber.email])
        page = Client().get(url)
        self.assertEqual(page.status_code, 200)
        self.assertTrue('form' in page.context)

    def getJson(self):
        import json
        districts = District.objects.all()
        entities = {}
        for district in districts:
            entities[district.pk] = True
        return json.dumps(entities)

    def test_validation_subscribe(self):
        self.assertEqual(Subscriber.objects.all().count(), 0)
        entity_json = self.getJson()
        validation = Validation.objects.create(email='test1@test.de', action='subscribe', entities=entity_json)
        validation.save()
        url = reverse('wbc.notifications.views.validate', args=[validation.code])
        page = Client().get(url)
        self.assertEqual(page.status_code, 200)
        self.assertEqual(page.context['success'], True)
        self.assertEqual(Validation.objects.all().count(), 0)
        self.assertEqual(Subscriber.objects.all().count(), 1)

    def test_validation_subscribe_subscriber_exits(self):
        subscriber = self.create_subscriber()
        self.assertEqual(Subscriber.objects.all().count(), 1)
        entity_json = self.getJson()
        validation = Validation.objects.create(email=subscriber.email, action='subscribe', entities=entity_json)
        validation.save()
        url = reverse('wbc.notifications.views.validate', args=[validation.code])
        page = Client().get(url)
        self.assertEqual(page.status_code, 200)
        self.assertEqual(page.context['success'], True)
        self.assertEqual(Validation.objects.all().count(), 0)
        self.assertEqual(Subscriber.objects.all().count(), 1)

    def test_validation_unsubscribe(self):
        subscriber = self.create_subscriber()
        count = Subscriber.objects.all().count()
        self.assertEqual(count, 1)
        entity_json = self.getJson()
        validation = Validation.objects.create(email=subscriber.email, action='unsubscribe', entities=entity_json)
        validation.save()
        url = reverse('wbc.notifications.views.validate', args=[validation.code])
        page = Client().get(url)
        self.assertEqual(page.status_code, 200)
        self.assertEqual(page.context['success'], True)
        self.assertEqual(Validation.objects.all().count(), 0)
        self.assertEqual(Subscriber.objects.all().count(), 0)

    def test_validation_unsubscribe_subscriber_does_not_exist(self):
        count = Subscriber.objects.all().count()
        self.assertEqual(count, 0)
        entity_json = self.getJson()
        validation = Validation.objects.create(email='hallo@example.com', action='unsubscribe', entities=entity_json)
        validation.save()
        url = reverse('wbc.notifications.views.validate', args=[validation.code])
        page = Client().get(url)
        self.assertEqual(page.status_code, 200)
        self.assertEqual(page.context['success'], True)
        self.assertEqual(Validation.objects.all().count(), 0)
        self.assertEqual(Subscriber.objects.all().count(), 0)

    def test_validation_wrong_action(self):
        count = Subscriber.objects.all().count()
        self.assertEqual(count, 0)
        entity_json = self.getJson()
        validation = Validation.objects.create(email='hallo@example.com', action='wrong_action', entities=entity_json)
        validation.save()
        url = reverse('wbc.notifications.views.validate', args=[validation.code])
        try:
            Client().get(url)
        except:
            error_occured = True
        self.assertTrue(error_occured)

    def test_validation_does_not_exist(self):
        url = reverse('wbc.notifications.views.validate', args=['abc'])
        page = Client().get(url)
        self.assertEqual(page.status_code, 200)
        self.assertFalse('success' in page.context)
        self.assertEqual(Validation.objects.all().count(), 0)
        self.assertEqual(Subscriber.objects.all().count(), 0)


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
