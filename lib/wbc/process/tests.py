# -*- coding: utf-8 -*-
from django.test import TestCase
from models import Place
from django.core.urlresolvers import reverse

from wbc.process.models import Place
from wbc.process.models import Publication
from wbc.process.models import ProcessStep
from wbc.process.models import ProcessType
from wbc.region.models import Department
from wbc.region.models import Muncipality
from wbc.region.models import District


class ProcessTestCase(TestCase):

    def setUp(self):
        a = Place(
            address='Unter den Linden 1',
            description='Brandenburger Tor',
            lat='-13',
            lon='52',
            identifier='ACB',
            active=False,
        )
        a.save()

        m = Muncipality(name='Berlin').save()

        d = District(
            name='Mitte')
        d.muncipality = Muncipality.objects.get(name='Berlin')
        d.save()

        b = District.objects.get(name='Mitte')
        a.entities.add(b)
        a.save()

        pt = ProcessType(
            name="BplanVerfahren", description="description")
        pt.save()

        ps = ProcessStep(name="Schritt1", description="description",
                         icon="abc", hover_icon="abc", order=1)
        ps.process_type = pt
        ps.save()

        d = Department(name="Gemeinde")
        d.entity = Muncipality.objects.get(name='Berlin')
        d.save()

    def create_place(self, address='Unter den Linden 1', description='Brandenburger Tor', lat='-13', lon='52', identifier='ACB', active=False):
        return Place.objects.create(
            address=address,
            description=description,
            lat=lat,
            lon=lon,
            identifier=identifier,
            active=active)

    def test_place(self):
        p = self.create_place()
        self.assertTrue(isinstance(p, Place))
        detail_url = reverse('place', kwargs={'pk': p.pk})
        self.assertEqual(p.get_absolute_url(), detail_url)
        update_url = reverse('place_update', kwargs={'pk': p.pk})
        self.assertEqual(p.get_update_url(), update_url)
        delete_url = reverse('place_delete', kwargs={'pk': p.pk})
        self.assertEqual(p.get_delete_url(), delete_url)
        strings = []
        if p.identifier:
            strings.append(p.identifier)
        if p.address:
            strings.append(p.address)
        self.assertEqual(
            p.__unicode__(), ', '.join(strings))

    def create_publication(self, description='Publication'):
        import datetime
        now = datetime.datetime.now()
        place = Place.objects.get(address='Unter den Linden 1')
        process_step = ProcessStep.objects.get(name="Schritt1")
        department = Department.objects.get(name="Gemeinde")
        return Publication.objects.create(
            process_step=process_step,
            description=description,
            place=place,
            begin=now,
            end=now + datetime.timedelta(days=3),
            department=department)

    def test_publication(self):
        p = self.create_publication()
        self.assertTrue(isinstance(p, Publication))
        detail_url = reverse('place', kwargs={'pk': p.place.pk})
        self.assertEqual(p.get_absolute_url(), detail_url)
        update_url = reverse('publication_update', kwargs={'pk': p.pk})
        self.assertEqual(p.get_update_url(), update_url)
        delete_url = reverse('publication_delete', kwargs={'pk': p.pk})
        self.assertEqual(p.get_delete_url(), delete_url)
        string = unicode(p.place) + ', ' + p.process_step.name
        self.assertEqual(p.__unicode__(), string)

    def test_process_step(self):
        ps = ProcessStep.objects.get(name="Schritt1")
        self.assertEqual(ps.__unicode__(), unicode(ps.process_type) + ', ' + ps.name)

    def test_process_type(self):
        pt = ProcessType.objects.get(name="BplanVerfahren")
        self.assertEqual(pt.__unicode__(), pt.name)
