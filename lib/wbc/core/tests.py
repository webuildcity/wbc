# -*- coding: utf-8 -*-
from django.test import TestCase
from django.contrib.auth.models import User
from wbc.core.forms import LoginForm
from django.test.client import RequestFactory


class CoreTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            'john', 'lennon@thebeatles.com', 'johnpassword')
        self.factory = RequestFactory()

    # form tests

    def test_valid_form(self):
        data = {'username': 'john', 'password': 'johnpassword'}
        form = LoginForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'username': '', 'password': ''}
        form = LoginForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_login(self):
        request = self.factory.post(
            '', {'username': 'john', 'password': 'johnpassword'})
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.login(request)
            self.assertTrue(user, self.user)
