# -*- coding: utf-8 -*-
import datetime

from django.test import TestCase, Client

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from wbc.projects.serializers import MapSerializer
from wbc.events.models import Publication
from wbc.process.models import ProcessStep, ProcessType
from wbc.stakeholder.models import Department
from wbc.region.models import Muncipality, District

from photologue.tests.factories import GalleryFactory,  PhotoFactory

from wbc.projects.models import *

class ProjectTestCase(TestCase):

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

        test_gallery = GalleryFactory()
        pl = PhotoFactory()
        pl2 = PhotoFactory()
        test_gallery.photos.add(pl)
        test_gallery.photos.add(pl2)

        project = Project(
            address='Unter den Linden 1',
            description='Brandenburger Tor',
            lat='-13',
            lon='52',
            identifier='ACB',
            name='ACB',
            active=False,
            gallery=test_gallery
        )
        project.save()
        project.entities.add(district)
        # project.events.add(p)
        project.save()
        self.project_id = project.pk

        publication = Publication(
            process_step=process_step,
            description='description',
            project=project,
            begin=now,
            end=now + datetime.timedelta(days=3),
            department=department
        )
        publication.save()
        self.publication_id = publication.pk

    # model tests

    def test_model_project(self):
        p = Project.objects.first()
        self.assertTrue(isinstance(p, Project))
        detail_url = reverse('project', kwargs={'pk': p.pk})
        self.assertEqual(p.get_absolute_url(), detail_url)
        update_url = reverse('project_update', kwargs={'pk': p.pk})
        self.assertEqual(p.get_update_url(), update_url)
        delete_url = reverse('project_delete', kwargs={'pk': p.pk})
        self.assertEqual(p.get_delete_url(), delete_url)
        strings = []
        if p.identifier:
            strings.append(p.identifier)
        if p.address:
            strings.append(p.address)
        self.assertEqual(
            p.__unicode__(), ', '.join(strings))

    #view tests
    def test_view_projects(self):
        url = reverse('projects')
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_project(self):
        url = reverse('project', args=[self.project_id])
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        detail_url = reverse('projectslug', kwargs={'slug':'acb'} )
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
        url = reverse('project_update', args=[self.project_id])

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

    def test_view_project_delete_get(self):
        url = reverse('project_delete', args=[self.project_id])

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

    def test_view_project_delete_post(self):
        url = reverse('project_delete', args=[self.project_id])

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
        url = '/project/map/%i/' % self.project_id
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
        url = '/project/projects/%i/' % self.project_id
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
        url = '/project/projects/%i/?geometry=polygon' % self.project_id
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

        url = '/project/projects/%i/?geometry=polygon' % self.project_id
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')


    # serializer test

    def test_serializer_map(self):
        queryset = Project.objects.get(pk=self.project_id)
        serializer = MapSerializer(queryset)
        self.assertEqual(serializer.data['identifier'],'ACB')