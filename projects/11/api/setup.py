#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

requirements = [
    'flask', 'flask-cors'
]

test_requirements = [
    'coverage'
]

setup(
    name='textmining-server',
    version='0.0.1',
    description="Text mining REST API server",
    url='',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    package_dir={'textmining-server':
                     'textmining-server'},
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
