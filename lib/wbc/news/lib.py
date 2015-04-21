# -*- coding: utf-8 -*-
from django.conf import settings
from django.template import loader, Context
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

def send_mail(to, template, context):
    if type(to) != list:
        to = [to,]

    t = loader.get_template(template)
    c = Context(context)

    html_part = t.render(c)
    text_part = strip_tags(html_part)

    subject,body = text_part.split('---')

    msg = EmailMultiAlternatives(subject.strip(),body.strip(),settings.EMAIL_FROM,to)

    return msg.send()
