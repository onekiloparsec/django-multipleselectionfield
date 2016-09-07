# -*- coding: utf-8 -*-

from django.db import models

from multipleselectionfield import MultipleSelectionField

CATEGORY_CHOICES = (
    (1, 'Handbooks and manuals by discipline'),
    (2, 'Business books'),
    (3, 'Books of literary criticism'),
    (4, 'Books about literary theory'),
    (5, 'Books about literature')
)

TAGS_CHOICES = (
    ('sex', 'Sex'),
    ('work', 'Work'),
    ('happy', 'Happy'),
    ('food', 'Food'),
    ('field', 'Field'),
    ('boring', 'Boring'),
    ('interesting', 'Interesting'),
    ('huge', 'huge'),
    ('nice', 'Nice'),
)


class Book(models.Model):
    title = models.CharField(max_length=200)
    categories = MultipleSelectionField(choices=CATEGORY_CHOICES, max_choices=3, default=1)
    tags = MultipleSelectionField(choices=TAGS_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.__str__()
