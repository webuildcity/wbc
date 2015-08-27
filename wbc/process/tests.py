# -*- coding: utf-8 -*-
import datetime

from django.test import TestCase
from django.test import Client

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from wbc.projects.serializers import MapSerializer
from wbc.projects.models import Project
from wbc.events.models import Publication
from wbc.process.models import ProcessStep
from wbc.process.models import ProcessType
from wbc.stakeholder.models import Department
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
        
        now = datetime.datetime.now()

        p = Publication(
            process_step=process_step,
            description='description',
            # Project=a,
            begin=now,
            end=now + datetime.timedelta(days=3),
            department=department
        )
        p.save()

        p2 = Publication(
            process_step=process_step,
            description='description',
            # Project=c,
            begin=now,
            end=now + datetime.timedelta(days=3),
            department=department
        )
        p2.save()

        a = Project(
            address='Unter den Linden 1',
            description='Brandenburger Tor',
            lat='-13',
            lon='52',
            identifier='ACB',
            active=False,
        )
        a.save()
        a.entities.add(district)
        a.events.add(p)
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
        b.events.add(p) 
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
        d.events.add(p)

        d.save()


    # model tests

    def test_model_Project(self):
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

    # def test_model_publication(self):
    #     p = Publication.objects.first()
    #     self.assertTrue(isinstance(p, Publication))
    #     # detail_url = reverse('project', kwargs={'pk': Project.objects.filter(events=p)[0].pk})
    #     # self.assertEqual(p.get_absolute_url(), detail_url)
    #     update_url = reverse('publication_update', kwargs={'pk': p.pk})
    #     self.assertEqual(p.get_update_url(), update_url)
    #     delete_url = reverse('publication_delete', kwargs={'pk': p.pk})
    #     self.assertEqual(p.get_delete_url(), delete_url)
    #     string = unicode(Project.objects.filter(events=p)[0]) + ', ' + p.process_step.name
    #     self.assertEqual(p.__unicode__(), string)

    def test_model_process_step(self):
        ps = ProcessStep.objects.get(name="ProcessStep")
        self.assertEqual(
            ps.__unicode__(), unicode(ps.process_type) + ', ' + ps.name)

    def test_model_process_type(self):
        pt = ProcessType.objects.get(name="ProcessType")
        self.assertEqual(pt.__unicode__(), pt.name)

    # view tests

    def test_view_process(self):
        url = reverse('process')
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_projects(self):
        url = reverse('projects')
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_project(self):
        url = reverse('project', args=['1'])
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
        url = reverse('project_update', args=['1'])

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
        url = reverse('project_delete', args=['2'])

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
        url = reverse('project_delete', args=['2'])

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
        url = '/project/map/1/'
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
        url = '/project/projects/1/'
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
        url = '/project/Projects/1/?geometry=polygon'
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

        url = '/project/projects/2/?geometry=polygon'
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')

    def test_api_publications(self):
        url = '/events/publications/'
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
        queryset = Project.objects.get(pk=4)
        serializer = MapSerializer(queryset)
        self.assertEqual(serializer.data['identifier'],'ACB')

    # admin test

    def test_admin_publication_add_get(self):
        url = '/admin/process/publication/add/'

        client = Client()

        # login
        client.post('/login/',{'username':'admin', 'password':'admin'})

        # try to GET when logged in
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
