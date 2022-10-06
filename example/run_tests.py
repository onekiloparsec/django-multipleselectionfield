#!/usr/bin/env python3
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

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
management.call_command('test', 'example.app')
