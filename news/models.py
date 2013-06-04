from django.db import models
from django.conf import settings
from templated_email import send_templated_mail

import random,string

class Validierung(models.Model):
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

class Abonent(models.Model):
    email   = models.EmailField(unique=True)
    bezirke = models.ManyToManyField('projekte.Bezirk', related_name='abonenten')
    
    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name        = "Abonent"
        verbose_name_plural = "Abonenten"

class Mail():
    def abonieren(self, to, code):
        send_templated_mail(
            template_name = 'abonieren',
            template_prefix = 'news/',
            from_email = settings.EMAIL_FROM,
            recipient_list = [to],
            context = {
                'abbestellen': settings.SITE_URL + '/news/abbestellen/' + to,
                'link': settings.SITE_URL + '/news/validieren/' + code
            }
        )

    def abbestellen(self, to, code):
        send_templated_mail(
            template_name = 'abbestellen',
            template_prefix = 'news/',
            from_email = settings.EMAIL_FROM,
            recipient_list = [to],
            context = {
                'link': settings.SITE_URL + '/news/validieren/' + code
            }
        )

    def newsletter(self, to, veroeffentlichungen):
        send_templated_mail(
            template_name = 'newsletter',
            template_prefix = 'news/',
            from_email = settings.EMAIL_FROM,
            recipient_list = [to],
            context = {
                'veroeffentlichungen': veroeffentlichungen,
                'projekt': settings.SITE_URL + '/projekt/',
                'abbestellen': settings.SITE_URL + '/news/abbestellen/' + to
            }
        )
