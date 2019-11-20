#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

requirements = [
    'SPARQLWrapper==1.8.4',
    'rdflib==4.2.2'
]

test_requirements = [
    'coverage'
]

setup(
    name='textminingservice-biokb',
    version='0.0.1',
    description="BioKB implementation of the common text mining interface",
    url='',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    package_dir={'textminingservice-biokb':
                     'textminingservice_biokb'},
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
    tests_require=test_requirements,
)
