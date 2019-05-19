#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import django

from django.conf import ENVIRONMENT_VARIABLE
from django.core import management


if len(sys.argv) == 1:
    os.environ[ENVIRONMENT_VARIABLE] = 'example.settings'
else:
    os.environ[ENVIRONMENT_VARIABLE] = sys.argv[1]

django.setup()

if django.VERSION[0] == 1 and django.VERSION[1] >= 7:
    from django.core.wsgi import get_wsgi_application

    application = get_wsgi_application()

if django.VERSION[0] == 1 and django.VERSION[1] <= 5:
    management.call_command('test', 'app')
else:
    management.call_command('test', 'example.app')
