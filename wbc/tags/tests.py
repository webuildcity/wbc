# -*- coding: utf-8 -*-
from django.test import TestCase, Client

from wbc.tags.models import *

class TagTestCase(TestCase):
    def setUp(self):
        t = WbcTag(
            name='tag'
        )
        t.save()

    # model tests
    def test_model_wbctag(self):
        t = WbcTag.objects.first()
        self.assertTrue(isinstance(t, WbcTag))
        self.assertEqual(t.__unicode__(), t.name)
        detail_url = reverse('tag', kwargs={'slug': t.slug})
        self.assertEqual(t.get_absolute_url(), detail_url)

    # view tests

    def test_view_tag(self):
        t = WbcTag.objects.first()
        url = reverse('tag', args=[t.slug])
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
