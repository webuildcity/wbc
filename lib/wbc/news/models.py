# -*- coding: utf-8 -*-
import random,string

from django.db import models
from django.conf import settings
from django.template import loader, Context
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

from wbc.core.models import Model
from wbc.process.models import Entity

class Validation(Model):
    email    = models.EmailField(unique=True)
    entities = models.CharField(max_length=256, blank=True, null=True)
    code     = models.SlugField(max_length=32)
    action   = models.CharField(max_length=16)

    def save(self, *args, **kwargs):
        c = string.ascii_lowercase + string.ascii_uppercase + string.digits
        self.code =''.join(random.sample(c*32,32))
        super(Validation, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name        = "Validierung"
        verbose_name_plural = "Validierung"

class Subscriber(Model):
    email    = models.EmailField(unique=True)
    entities = models.ManyToManyField(Entity, related_name='subscribers')

    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name        = "Abonnent"
        verbose_name_plural = "Abonnenten"

class Mail():
    def subscribe(self, to, code):
        self.send(to, settings.NEWS_SUBJECT_SUBSCRIBE,
            'news/mail/subscribe.html', {
                'unsubscribe': settings.SITE_URL + '/news/unsubscribe/' + to,
                'link': settings.SITE_URL + '/news/validation/' + code
            })

    def unsubscribe(self, to, code):
        self.send(to, settings.NEWS_SUBJECT_UNSUBSCRIBE,
            'news/mail/unsubscribe.html', {
                'link': settings.SITE_URL + '/news/validation/' + code
            })

    def newsletter(self, to, publications):
        self.send(to, settings.NEWS_SUBJECT_NEWSLETTER,
            'news/mail/newsletter.html', {
            'publications': publications,
            'ort': settings.SITE_URL + '/orte/',
            'unsubscribe': settings.SITE_URL + '/news/validation/' + to
        })

    def send(self, to, subject, template, context):
        if type(to) != list:
            to = [to,]

        t = loader.get_template(template)
        c = Context(context)

        html_part = t.render(c)
        text_part = strip_tags(html_part)

        msg = EmailMultiAlternatives(subject,text_part,settings.EMAIL_FROM,to)

        return msg.send()
