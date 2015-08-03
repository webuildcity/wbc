# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from django.test.client import RequestFactory
from django.core.urlresolvers import reverse

from wbc.core.forms import LoginForm
from wbc.region.models import District
from wbc.region.models import Muncipality


# form tests

class CoreFormTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='john', email='lennon@thebeatles.com', password='johnpassword')
        self.factory = RequestFactory()

    def test_valid_form(self):
        request = self.factory.post(
            '', {'username': 'john', 'password': 'johnpassword'})
        form = LoginForm(request.POST)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        request = self.factory.post(
            '', {'username': 'john', 'password': ''})
        form = LoginForm(request.POST)
        self.assertFalse(form.is_valid())

    def test_form_login(self):
        request = self.factory.post('', {'username': 'john', 'password': 'johnpassword'})
        form = LoginForm(request.POST)
        self.assertTrue(form.is_valid())
        user = form.login(request)
        self.assertTrue(user, self.user)

# view tests

class CoreViewTestCase(TestCase):

    def setUp(self):
        Muncipality(name='Berlin').save()

        self.d1 = District(
            name='Mitte',
            muncipality=Muncipality.objects.get(name='Berlin')
        )
        self.d1.save()

        self.d2 = District(
            name='Charlottenburg',
            muncipality=Muncipality.objects.get(name='Berlin')
        )
        self.d2.save()
        self.user = User.objects.create_user(
            username='john', email='lennon@thebeatles.com', password='johnpassword')

        self.factory = RequestFactory()

    def test_view_feeds(self):
        url = reverse('wbc.core.views.feeds')
        resp = Client().get(url)
        self.assertEqual(resp.status_code, 200)

    def test_view_login_success(self):
        url = reverse('wbc.core.views.login_user')
        resp = Client().post(
            url, {'username': self.user.username, 'password': 'johnpassword'})
        self.assertEqual(resp.status_code, 302)

    def test_view_login_success_next(self):
        url = reverse('wbc.core.views.login_user')
        resp = Client().post(
            url, {'username': self.user.username, 'password': 'johnpassword', 'next': '/liste'})
        self.assertEqual(resp.status_code, 302)

    def test_view_login_fail(self):
        url = reverse('wbc.core.views.login_user')
        resp = Client().post(
            url, {'username': self.user.username, 'password': ''})
        self.assertEqual(resp.status_code, 200)

    def test_view_logout(self):
        url = reverse('wbc.core.views.logout_user')
        resp = Client().get(url)
        self.assertEqual(resp.status_code, 200)
