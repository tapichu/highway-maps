#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

def fread(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "highway-maps",
    version = "1.0",
    url = "https://github.com/tapichu/highway-maps",
    license = "MIT",
    description = "Search highways and draw them on google maps",
    long_description = fread('README'),
    keywords = "django backbone requirejs",

    author = "Eduardo López Biagi",
    author_email = "eduardo.biagi@gmail.com",

    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,

    install_requires = [
        'setuptools',
        'simplejson',
    ],

    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)

