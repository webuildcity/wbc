# -*- coding: utf-8 -*-
import datetime

from django.test import TestCase
from django.test import Client

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from wbc.process.serializers import MapSerializer
from wbc.process.models import Place
from wbc.process.models import Publication
from wbc.process.models import ProcessStep
from wbc.process.models import ProcessType
from wbc.region.models import Department
from wbc.region.models import Muncipality
from wbc.region.models import District


class ProcessTestCase(TestCase):

    def setUp(self):
        User.objects.create_superuser('admin', 'admin@example', 'admin')

        muncipality = Muncipality(name='Berlin')
        muncipality.save()

        district = District(name='Mitte')
        district.muncipality = muncipality
        district.save()

        process_type = ProcessType(name="ProcessType", description="description")
        process_type.save()

        process_step = ProcessStep(name="ProcessStep", description="description",
                         icon="abc", hover_icon="abc", order=1)
        process_step.process_type = process_type
        process_step.save()

        department = Department(name="Department")
        department.entity = muncipality
        department.save()

        a = Place(
            address='Unter den Linden 1',
            description='Brandenburger Tor',
            lat='-13',
            lon='52',
            identifier='A',
            active=False,
        )
        a.save()
        a.entities.add(district)
        a.save()
        self.place_id = a.pk

        now = datetime.datetime.now()
        p = Publication(
            process_step=process_step,
            description='description',
            place=a,
            begin=now,
            end=now + datetime.timedelta(days=3),
            department=department
        )
        p.save()
        self.publication_id = p.pk

    # model tests

    def test_model_place(self):
        p = Place.objects.get(pk=self.place_id)
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
        self.assertEqual(p.__unicode__(), ', '.join(strings))

    def test_model_publication(self):
        p = Publication.objects.get(pk=self.publication_id)
        self.assertTrue(isinstance(p, Publication))

        detail_url = reverse('place', kwargs={'pk': p.place.pk})
        self.assertEqual(p.get_absolute_url(), detail_url)

        update_url = reverse('publication_update', kwargs={'pk': p.pk})
        self.assertEqual(p.get_update_url(), update_url)

        delete_url = reverse('publication_delete', kwargs={'pk': p.pk})
        self.assertEqual(p.get_delete_url(), delete_url)

        string = str(p.place) + ', ' + p.process_step.name
        self.assertEqual(p.__str__(), string)

    def test_model_process_step(self):
        ps = ProcessStep.objects.get(name="ProcessStep")
        self.assertEqual(ps.__str__(), str(ps.process_type) + ', ' + ps.name)

    def test_model_process_type(self):
        pt = ProcessType.objects.get(name="ProcessType")
        self.assertEqual(pt.__unicode__(), pt.name)

    # view tests

    def test_view_process(self):
        url = reverse('process')
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_places(self):
        url = reverse('places')
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_place(self):
        url = reverse('place', args=[self.place_id])
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_feed(self):
        url = reverse('publication_feed_url')

        response = Client().get(url)
        self.assertEqual(response.status_code, 200)

        response = Client().get(url + '?bezirk=Mitte')
        self.assertEqual(response.status_code, 200)

        response = Client().get(url + '?bezirk=foobar')
        self.assertEqual(response.status_code, 404)

    def test_view_place_create_get(self):
        url = reverse('place_create')

        client = Client()

        # try to GET when not logged in
        response = client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(url in response.url)

        # login
        client.login(username='admin', password='admin')

        # try to GET when logged in
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)

    def test_view_place_update_get(self):
        url = reverse('place_update', args=[self.place_id])

        client = Client()

        # try to GET when not logged in
        response = client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(url in response.url)

        # login
        client.login(username='admin', password='admin')

        # try to GET when logged in
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)

    def test_view_place_delete_get(self):
        url = reverse('place_delete', args=[self.place_id])

        client = Client()

        # try to GET when not logged in
        response = client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(url in response.url)

        # login
        client.login(username='admin', password='admin')

        # try to GET when logged in
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_place_delete_post(self):
        url = reverse('place_delete', args=[self.place_id])

        client = Client()

        # try to POST when not logged in
        response = client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(url in response.url)

        # login
        client.login(username='admin', password='admin')

        # try to POST when logged in
        response = client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.endswith(reverse('places'))) # should redirect to '/liste/'

    def test_view_publication_create_get(self):
        url = reverse('publication_create')

        client = Client()

        # try to GET when not logged in
        response = client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(url in response.url)

        # login
        client.login(username='admin', password='admin')

        # try to GET when logged in
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)

    def test_view_publication_create_get_place_id(self):
        url = reverse('publication_create')

        client = Client()

        # try to GET when not logged in
        response = client.get(url + '?place_id=%i' % self.place_id)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(url in response.url)

        # login
        client.login(username='admin', password='admin')

        # try to GET when logged in
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)

    def test_view_publication_update_get(self):
        url = reverse('publication_update', args=[self.publication_id])

        client = Client()

        # try to GET when not logged in
        response = client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(url in response.url)

        # login
        client.login(username='admin', password='admin')

        # try to GET when logged in
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)

    def test_view_publication_delete_get(self):
        url = reverse('publication_delete', args=[self.publication_id])

        client = Client()

        # try to GET when not logged in
        response = client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(url in response.url)

        # login
        client.login(username='admin', password='admin')

        # try to GET when logged in
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_publication_delete_post(self):
        url = reverse('publication_delete', args=[self.publication_id])

        client = Client()

        # try to POST when not logged in
        response = client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(url in response.url)

        # login
        client.login(username='admin', password='admin')

        # try to POST when logged in
        response = client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.endswith(reverse('place', args=[self.place_id]))) # should redirect to '/liste/'

    # rest api tests

    def test_api_list(self):
        url = '/process/list/'
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

    def test_api_list_search(self):
        url = '/process/list/?search=Brandenburger'
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

    def test_api_map(self):
        url = '/process/map/'
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

    def test_api_mapitem(self):
        url = '/process/places/%i/' % self.place_id
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

    def test_api_places(self):
        url = '/process/places/'
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

    def test_api_places_active(self):
        url = '/process/places/?active=1'
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

    def test_api_place(self):
        url = '/process/places/%i/' % self.place_id
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

    def test_api_places_point(self):
        url = '/process/places/%i/?geometry=point' % self.place_id
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

    def test_api_places_polygon(self):
        url = '/process/places/?geometry=polygon'
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

    def test_api_place_polygon(self):
        url = '/process/places/%i/?geometry=polygon' % self.place_id
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

        url = '/process/places/%i/?geometry=polygon' % self.place_id
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

    def test_api_publications(self):
        url = '/process/publications/'
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

    def test_api_processsteps(self):
        url = '/process/processsteps/'
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

    def test_api_processtypes(self):
        url = '/process/processtypes/'
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

    # serializer test

    def test_serializer_map(self):
        queryset = Place.objects.get(pk=self.place_id)
        serializer = MapSerializer(queryset)
        self.assertEqual(serializer.data['identifier'],'A')

    # admin test

    def test_admin_publication_add_get(self):
        url = '/admin/process/publication/add/'

        client = Client()

        # login
        client.post('/login/',{'username':'admin', 'password':'admin'})

        # try to GET when logged in
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
