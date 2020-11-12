#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='myproject',
      version='1.0',
      packages=find_packages(),
      scripts=['manage.py'])
      
manage.py migrate --noinput
manage.py runserver
