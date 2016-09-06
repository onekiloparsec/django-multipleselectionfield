django-multiplechoicesfield
=======================

.. image:: https://travis-ci.org/goinnn/django-multiplechoicesfield.png?branch=master
    :target: https://travis-ci.org/goinnn/django-multiplechoicesfield

.. image:: https://coveralls.io/repos/goinnn/django-multiplechoicesfield/badge.png?branch=master
    :target: https://coveralls.io/r/goinnn/django-multiplechoicesfield

.. image:: https://badge.fury.io/py/django-multiplechoicesfield.png
    :target: https://badge.fury.io/py/django-multiplechoicesfield

.. image:: https://pypip.in/d/django-multiplechoicesfield/badge.png
    :target: https://pypi.python.org/pypi/django-multiplechoicesfield

A new model and form field. With this you can get a multiple select from a choices

Initial code got from https://github.com/goinnn/django-multiselectfield by Pablo Martin

But after more than 2 years without activity and no fork taking the control of it, it may be time
to move on. Here is an attempt of a small renaming (to avoid name conflicts in packages),
and including the improvements of most of the existing forks.

The LPGL v3 licence is preserved.

Originally, this egg is inspired by this `snippet <http://djangosnippets.org/snippets/1200/>`_


Installation
============


In your models.py
-----------------

::

    from multiplechoicesfield import MultiSelectField

    ...

    MY_CHOICES = (('item_key1', 'Item title 1.1'),
                  ('item_key2', 'Item title 1.2'),
                  ('item_key3', 'Item title 1.3'),
                  ('item_key4', 'Item title 1.4'),
                  ('item_key5', 'Item title 1.5'))

    MY_CHOICES2 = ((1, 'Item title 2.1'),
                   (2, 'Item title 2.2'),
                   (3, 'Item title 2.3'),
                   (4, 'Item title 2.4'),
                   (5, 'Item title 2.5'))

    class MyModel(models.Model):

        .....

        my_field = MultipleChoicesField(choices=MY_CHOICES)
        my_field2 = MultipleChoicesField(choices=MY_CHOICES2,
                                     max_choices=3,
                                     max_length=3)


In your settings.py
-------------------

Only you need it, if you want the translation of django-multiplechoicesfield

::

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.admin',

        #.....................#

        'multiplechoicesfield',
    )



Example project
===============

In the source tree, you will find a directory called  
`example <https://github.com/onekiloparsec/django-multiplechoicesfield/tree/master/example/>`_. 
It contains a readily setup project that uses django-multiplechoicesfield. You can run it as usual:

::

    python manage.py syncdb --noinput
    python manage.py loaddata app_data
    python manage.py runserver
