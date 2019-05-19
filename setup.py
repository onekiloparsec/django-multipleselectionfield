# -*- coding: utf-8 -*-
# Copyright (c) 2016 by Cédric Foellmi <cedric@onekilopars.ec>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this programe.  If not, see <http://www.gnu.org/licenses/>.

# Initial code got from https://github.com/goinnn/django-multiselectfield by Pablo Martin
#
# September 2016:
# After more than 2 years without activity and no fork taking the control of it, I
# attempt a renaming with merge of most of the forks advances.
# The LPGL v3 licence is preserved.
#

import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name="django-multipleselectionfield",
    version="1.0.0",
    author="Cédric Foellmi",
    author_email="cedric@onekiloparsec.dev",
    description="Django multiple choices field",
    long_description=(read('README.md') + '\n\n' + read('CHANGES.md')),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    license="LGPL 3",
    keywords="django,multiple,select,field,choices",
    url='https://github.com/onekiloparsec/django-multipleselectionfield',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
