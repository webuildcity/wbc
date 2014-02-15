# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.template import loader, Context
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
import random,string

from lib.models import Model

class Validierung(Model):
    email   = models.EmailField(unique=True)
    bezirke = models.CharField(max_length=256, blank=True, null=True)
    code    = models.SlugField(max_length=32)
    aktion  = models.CharField(max_length=16)

    def save(self, *args, **kwargs):
        c = string.ascii_lowercase + string.ascii_uppercase + string.digits
        self.code =''.join(random.sample(c*32,32))
        super(Validierung, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name        = "Validierung"
        verbose_name_plural = "Validierung"

class Abonnent(Model):
    email   = models.EmailField(unique=True)
    bezirke = models.ManyToManyField('projects.Bezirk', related_name='abonnenten')
    
    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name        = "Abonnent"
        verbose_name_plural = "Abonnenten"

class Mail():
    def abonnieren(self, to, code):
        self.send(to, '[Bürger baut Stadt] Newsletter abonnieren',
            'news/mail/abonnieren.html', {
                'abbestellen': settings.SITE_URL + '/news/abbestellen/' + to,
                'link': settings.SITE_URL + '/news/validieren/' + code
            })

    def abbestellen(self, to, code):
        self.send(to, '[Bürger baut Stadt] Newsletter abbestellen',
            'news/mail/abbestellen.html', {
                'link': settings.SITE_URL + '/news/validieren/' + code
            })

    def newsletter(self, to, veroeffentlichungen):
        self.send(to, '[Bürger baut Stadt] Neue Veröffentlichungen',
            'news/mail/newsletter.html', {
            'veroeffentlichungen': veroeffentlichungen,
            'ort': settings.SITE_URL + '/orte/',
            'abbestellen': settings.SITE_URL + '/news/abbestellen/' + to
        })
        
    def send(self, to, subject, template, context):
        if type(to) != list:
            to = [to,]

        t = loader.get_template(template)
        c = Context(context)

        html_part = t.render(c)
        text_part = strip_tags(html_part)

        msg = EmailMultiAlternatives(subject,text_part,settings.EMAIL_FROM,to)
        #msg.attach_alternative(html_part, "text/html")

        return msg.send()