# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f: description = f.read()

install_requires = [
    'Django==1.8',
    'django-widget-tweaks==1.3',
    'markdown==2.3.1',
    'psycopg2>=2.5.1,<2.6',
    'djangorestframework>=3.1,<3.2',
    'djangorestframework-gis'
]

setup(
    name='we-build-city',
    url='https://github.com/webuildcity/wbc/',
    version='0.1.0',
    packages=find_packages(),
    license=u'GNU Lesser General Public License v3 (LGPLv3)',
    author=u'Magdalena Noffke, Jochen Klar, Timo Lundelius',
    maintainer=u'Magdalena Noffke, Jochen Klar, Timo Lundelius',
    maintainer_email=u'info@we-build.city',
    description=u'Finde geplante Bauvorhaben in deinem Kiez.',
    long_description=description,
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