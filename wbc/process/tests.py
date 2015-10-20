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

        project = Project(
            address='Unter den Linden 1',
            description='Brandenburger Tor',
            lat='-13',
            lon='52',
            identifier='A',
            active=False,
        )
        project.save()
        project.entities.add(district)
        project.save()
        self.project_id = project.pk

        now = datetime.datetime.now()
        publication1 = Publication(
            process_step=process_step,
            description='description',
            project=project,
            begin=now,
            end=now + datetime.timedelta(days=3),
            department=department
        )
        publication1.save()
        self.publication1_id = publication1.pk

        publication2 = Publication(
            process_step=process_step,
            description='description',
            project=project,
            begin=now,
            end=now + datetime.timedelta(days=3),
            department=department
        )
        publication2.save()
        self.publication2_id = publication2.pk

    # model tests

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

    # api test

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
