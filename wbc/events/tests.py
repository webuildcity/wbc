# -*- coding: utf-8 -*-
import datetime

from django.test import TestCase, Client

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from wbc.projects.serializers import MapSerializer
from wbc.projects.models import Project
from wbc.process.models import ProcessStep, ProcessType
from wbc.stakeholder.models import Department
from wbc.region.models import Muncipality, District

from wbc.events.models import *

class EventTestCase(TestCase):
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
        
        now = datetime.datetime.now()

        a = Project(
            address='Unter den Linden 1',
            description='Brandenburger Tor',
            name='name',
            lat='-13',
            lon='52',
            identifier='ACB',
            active=False,
        )
        a.save()
        a.entities.add(district)
        # a.events.add(p)
        a.save()

        b = Project(
            address='Unter den Linden 2',
            description='Brandenburger Tor',
            lat='-13',
            lon='52',
            identifier='ACB',
            active=False,
            polygon='[]'
        )
        b.save()
        b.entities.add(district)
        # b.events.add(p) 
        b.save()

        c = Project(
            address='Unter den Linden 3',
            description='Brandenburger Tor',
            lat='-13',
            lon='52',
            identifier='ACB',
            active=False,
            polygon='[]'
        )
        c.save()

        d = Project(
            address='Unter den Linden 4',
            description='Brandenburger Tor',
            lat='-13',
            lon='52',
            identifier='ACB',
            active=False,
            polygon='[]'
        )
        d.save()
        d.entities.add(district)
        # d.events.add(p)

        d.save()

        p = Publication(
            process_step=process_step,
            description='description',
            project=a,
            begin=now,
            end=now + datetime.timedelta(days=3),
            department=department
        )
        p.save()

        p2 = Publication(
            process_step=process_step,
            description='description',
            project=c,
            begin=now + datetime.timedelta(days=3),
            end=now + datetime.timedelta(days=6),
            department=department
        )
        p2.save()

        p3 = Publication(
            process_step=process_step,
            description='description',
            project=c,
            begin=now - datetime.timedelta(days=6),
            end=now - datetime.timedelta(days=3),
            department=department
        )
        p3.save()


        e = Event(
            title='title',
            description='description',
            begin=now,
            end=now + datetime.timedelta(days=3)
        )
        e.save()
    #model tests

    def test_model_publication(self):
        p = Publication.objects.filter(pk=1)[0]
        p2 = Publication.objects.filter(pk=2)[0]
        p3 = Publication.objects.filter(pk=3)[0]
        self.assertTrue(isinstance(p, Publication))
        detail_url = reverse('project', kwargs={'pk': p.project.pk})
        self.assertEqual(p.get_absolute_url(), detail_url)
        update_url = reverse('publication_update', kwargs={'pk': p.pk})
        self.assertEqual(p.get_update_url(), update_url)
        delete_url = reverse('publication_delete', kwargs={'pk': p.pk})
        self.assertEqual(p.get_delete_url(), delete_url)
        string = unicode(p.project) + ', ' + p.process_step.name
        self.assertEqual(p.__unicode__(), string)
        
        self.assertTrue(p.is_started())
        self.assertEqual(p.is_in_past(), False)
        self.assertTrue(p3.is_in_past())
        self.assertEqual(p2.is_started(), False)

    def test_model_event(self):
        e = Event.objects.first()
        self.assertTrue(isinstance(e, Event))
        string = unicode(e.title)
        self.assertEqual(e.__unicode__(), string)


    #view tests

    def test_view_feed(self):
        url = reverse('publication_feed_url')

        response = Client().get(url)
        self.assertEqual(response.status_code, 200)

        response = Client().get(url + '?bezirk=Mitte')
        self.assertEqual(response.status_code, 200)

        response = Client().get(url + '?bezirk=foobar')
        self.assertEqual(response.status_code, 404)


    def test_view_publication_create_get(self):
        url = reverse('publication_create')

        client = Client()

        # try to GET when not logged in
        response = client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(url in response.url)

        # login
        client.post('/login/',{'username':'admin', 'password':'admin'})

        # try to GET when logged in
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)

    def test_view_publication_create_get_Project_id(self):
        url = reverse('publication_create')

        client = Client()

        # try to GET when not logged in
        response = client.get(url + '?project_id=1')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(url in response.url)

        # login
        client.post('/login/',{'username':'admin', 'password':'admin'})

        # try to GET when logged in
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)

    def test_view_publication_update_get(self):
        url = reverse('publication_update', args=['1'])

        client = Client()

        # try to GET when not logged in
        response = client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(url in response.url)

        # login
        client.post('/login/',{'username':'admin', 'password':'admin'})

        # try to GET when logged in
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)

    def test_view_publication_delete_get(self):
        url = reverse('publication_delete', args=['1'])

        client = Client()

        # try to GET when not logged in
        response = client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(url in response.url)

        # login
        client.post('/login/',{'username':'admin', 'password':'admin'})

        # try to GET when logged in
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_publication_delete_post(self):
        url = reverse('publication_delete', args=['1'])

        client = Client()

        # try to POST when not logged in
        response = client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(url in response.url)

        # login
        client.post('/login/',{'username':'admin', 'password':'admin'})

        # try to POST when logged in
        response = client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.endswith(reverse('project', args=['1']))) # should redirect to '/liste/'

    # rest api tests

    def test_api_publications(self):
        url = '/events/publications/'
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

    # admin test

    def test_admin_publication_add_get(self):
        url = '/admin/events/publication/add/'

        client = Client()

        # login
        client.post('/login/',{'username':'admin', 'password':'admin'})

        # try to GET when logged in
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
