# -*- coding: utf-8 -*-
from django.test import TestCase, Client
from django.contrib.auth import login
from django.contrib.auth.models import User

import datetime

from wbc.projects.models import *

from wbc.projects.serializers import MapSerializer

class ProjectTestCase(TestCase):

    fixtures = [
        'fixtures_tests/auth/auth.json', 
        'fixtures_tests/process/process.json', 
        'fixtures_tests/events/events.json', 
        'fixtures_tests/projects/projects.json', 
    ]

    def setUp(self):
        self.p = Project.objects.first()

        address = Address(street="Teststreet", streetnumber="1", zipcode="34567")

        bufferArea = BufferArea(name="New Bufferarea", active=False)
        bufferArea.save()
        print "setup"

    def tearDowm(self):
        print "tearDown"

    def test_model_project(self):
        login = self.client.login(username='admin', password='123')
        print login
        
        user = User.objects.get(pk=1)
        p = Project.objects.first()
        print p.bufferarea_set.all()

        self.assertEqual(p.get_created_by(), User.objects.get(pk=p.history.last().history_user_id))
        # change not working?!
        # self.assertEqual(p.get_changed_by(), User.objects.get(pk=p.history.first().history_user_id))
        
        self.assertTrue(isinstance(p, Project))
        
        detail_url = reverse('projectslug', kwargs={'slug': p.slug})
        self.assertEqual(p.get_absolute_url(), detail_url)
        update_url = reverse('project_update', kwargs={'pk': p.pk})
        self.assertEqual(p.get_update_url(), update_url)
        delete_url = reverse('project_delete', kwargs={'pk': p.pk})
        self.assertEqual(p.get_delete_url(), delete_url)
        
        strings = []
        if p.name:
            strings.append(p.name)
        # if p.address:
        #     strings.append(p.address)
        self.assertEqual(
            p.__unicode__(), ', '.join(strings))

        today = datetime.datetime.today()
        next_date = p.events.filter(begin__gte=today, date__isnull=False).order_by('begin').first()
        self.assertEqual(p.get_next_date(), next_date)

        last_news = p.events.filter(media__isnull=False).order_by('begin').first()
        self.assertEqual(p.get_last_news(), last_news)

        self.assertEqual(p.terminated(), p.publication_set.filter(process_step__name="Feststellung")[0].begin)

        self.assertEqual(p.has_buffer_area(), p.bufferarea_set.all() > 0)

        # check how to delete pads than do this
        # self.assertTrue(p.get_pad_id() in p.padId)
        # self.assertTrue(p.get_group_id() in p.padId)

    def test_view_projects(self):
        url = reverse('projects')
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_project(self):
        p = Project.objects.first()

        url = reverse('project', args=[p.pk])
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        detail_url = reverse('projectslug', kwargs={'slug':p.slug} )
        response = Client().get(detail_url)
        self.assertEqual(response.status_code, 200)


    def test_view_project_create_get(self):
        url = reverse('project_create')

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

    def test_view_project_update_get(self):
        url = reverse('project_update', args=[self.p.pk])

        client = Client()

        # try to GET when not logged in
        response = client.get(url)
        self.assertEqual(response.status_code, 403)
        # self.assertTrue(url in response.url)

        # login
        client.post('/login/',{'username':'admin', 'password':'admin'})

        # try to GET when logged in
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)

    def test_view_project_delete_get(self):
        url = reverse('project_delete', args=[self.p.pk])

        client = Client()

        # try to GET when not logged in
        response = client.get(url)
        self.assertEqual(response.status_code, 403)
        # self.assertTrue(url in response.url)

        # login
        client.post('/login/',{'username':'admin', 'password':'admin'})

        # try to GET when logged in
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_project_delete_post(self):

        url = reverse('project_delete', args=[self.p.pk])

        client = Client()

        # try to POST when not logged in
        response = client.post(url)
        self.assertEqual(response.status_code, 403)
        # self.assertTrue(url in response.url)

        # login
        client.post('/login/',{'username':'admin', 'password':'123'})

        # try to POST when logged in
        response = client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.endswith(reverse('projects'))) # should redirect to '/liste/'


    # rest api tests

    def test_api_list(self):
        url = '/project/list/'
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

    def test_api_list_search(self):
        url = '/project/list/?search=Brandenburger'
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

    def test_api_map(self):
        url = '/project/map/'
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

    def test_api_mapitem(self):
        url = '/project/map/%i/' % self.p.pk
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

    def test_api_projects(self):
        url = '/project/projects/'
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

    def test_api_projects_active(self):
        url = '/project/projects/?active=1'
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

    def test_api_project(self):
        url = '/project/projects/%i/' % self.p.pk
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

    def test_api_projects_point(self):
        url = '/project/projects/?geometry=point'
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

    def test_api_projects_polygon(self):
        url = '/project/projects/?geometry=polygon'
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

    def test_api_project_polygon(self):
        url = '/project/projects/%i/?geometry=polygon' % self.p.pk
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

        url = '/project/projects/%i/?geometry=polygon' % self.p.pk
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')


    # serializer test

    # def test_serializer_map(self):
    #     queryset = Project.objects.get(pk=self.p.pk)
    #     serializer = MapSerializer(queryset)
    #     self.assertEqual(serializer.data['name'],'Test Projekt')