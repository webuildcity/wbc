#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os,datetime,json,urllib2
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

if os.path.isfile('bbs/settings.py'):
    sys.path.append(os.getcwd())
else:
    sys.exit('Error: not in the root directory of the django project.');

os.environ['DJANGO_SETTINGS_MODULE'] = 'bbs.settings'

os.chdir('../bvvscrape/')
os.system('rm -f data/json/*.json data/text/*.txt')
os.system('casperjs senat.js')
os.system('casperjs parlament.js')

subject = '[Bürger baut Stadt] bvvscrape'

text    = ''
for filename in os.listdir('data/text/'):
    if filename.endswith('.txt'):
        text += open('data/text/' + filename).read()

msg = EmailMultiAlternatives(subject,text,settings.EMAIL_FROM,('admin@jochenklar.de','info@buergerbautstadt.de'))
msg.send()
