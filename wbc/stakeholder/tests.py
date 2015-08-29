# -*- coding: utf-8 -*-
from django.test import TestCase, Client

from wbc.stakeholder.models import *

class StakeholderTestCase(TestCase):
    def setUp(self):
        # User.objects.create_superuser('admin', 'admin@example', 'admin')
        sr = StakeholderRole(
            role="rolle"
        )
        sr.save()
        s = Stakeholder(
            name="stakeholder"
        )
        s.save()
        s.roles.add(sr);
        s.save()

    # model tests
    def test_model_stakeholder(self):
        s = Stakeholder.objects.first()
        self.assertTrue(isinstance(s, Stakeholder))

        self.assertEqual(s.__unicode__(), s.name)
        detail_url = reverse('stakeholder', kwargs={'slug': s.slug})

        self.assertEqual(s.get_absolute_url(), detail_url)


    def test_model_stakeholderrole(self):
        sr = StakeholderRole.objects.first()
        self.assertEqual(sr.__unicode__(), sr.role)
        # detail_url = reverse('stakeholderrole', kwargs={'slug': s.slug})

        # self.assertEqual(s.get_absolute_url(), detail_url)


    # view test
    def test_view_stakeholder(self):
        s = Stakeholder.objects.first()
        url = reverse('stakeholder', args=[s.slug])
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
