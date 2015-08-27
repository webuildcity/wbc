# -*- coding: utf-8 -*-
from django.test import TestCase

from wbc.region.models import *


class RegionTestCase(TestCase):

    def setUp(self):
        Muncipality(name='Berlin').save()

    # To test a method of an abstract class, test a non-abstrct child class

    def create_muncipality(name='Hamburg'):
        m = Muncipality.objects.create(name=name)
        return m

    def test_muncipality(self):
        m = self.create_muncipality()
        self.assertEqual(
            m.__unicode__(), m.name)

    # def create_department(name='department'):
    #     m = Muncipality.objects.get(name='Berlin')
    #     d = Department.objects.create(name=name, entity=m)
    #     return d

    # def test_department(self):
    #     d = self.create_department()
    #     self.assertEqual(
    #         d.__unicode__(), d.name)
