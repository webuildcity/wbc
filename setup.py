# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = '0.1.2'

install_requires = [
    'Django==1.8',
    'django-widget-tweaks==1.3',
    'markdown==2.3.1',
    'djangorestframework==3.1',
    'djangorestframework-gis',
]

setup(
    name='django-wbc',
    version=version,
    url='https://github.com/webuildcity/wbc/',
    download_url='https://github.com/webuildcity/wbc/archive/%s.tar.gz' % version,
    packages=find_packages(),
    license=u'GNU Lesser General Public License v3 (LGPLv3)',
    author=u'Magdalena Noffke, Jochen Klar, Timo Lundelius, Umut Tas, Volker Eichhorn',
    author_email='info@we-build.city',
    maintainer=u'Jochen Klar',
    maintainer_email=u'jochenklar@gmail.com',
    description=u'We-build.city is a Django module for a collaboration platform about participation in urban planning.',
    include_package_data=True,
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Framework :: Django :: 1.8',
        'Natural Language :: German'
    ]
)
