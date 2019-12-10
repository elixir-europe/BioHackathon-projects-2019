#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

requirements = [
    'asyncio'
]

test_requirements = [
    'coverage'
]

setup(
    name='textminingservice-interface',
    version='0.0.1',
    description="Provides common interface to several text-mining services",
    url='',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    package_dir={'textminingservice':
                 'textminingservice'},
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
