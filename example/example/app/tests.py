# -*- coding: utf-8 -*-


from django.core.exceptions import ValidationError
from django.forms.models import modelform_factory
from django.test import TestCase

from example.app.models import Book


class MultiSelectTestCase(TestCase):

    fixtures = ['app_data.json']

    def test_filter(self):
        self.assertEqual(Book.objects.filter(tags__contains='sex').count(), 1)
        self.assertEqual(Book.objects.filter(tags__contains='boring').count(), 0)

    def test_form(self):
        form_class = modelform_factory(Book, fields=['title', 'categories', 'tags'])
        self.assertEqual(len(form_class.base_fields), 3)
        form = form_class({'title': 'new book',
                           'categories': '1,2'})
        if form.is_valid():
            form.save()

    def test_object(self):
        book = Book.objects.get(id=1)
        self.assertEqual(book.get_tags_display(), 'Sex, Work, Happy')
        self.assertEqual(book.get_tags_list(), ['Sex', 'Work', 'Happy'])
        self.assertEqual(book.get_categories_display(), 'Handbooks and manuals by discipline, Books of literary criticism, Books about literature')
        self.assertEqual(book.get_categories_list(), ['Handbooks and manuals by discipline', 'Books of literary criticism', 'Books about literature'])

        self.assertEqual(book.get_tags_list(), book.get_tags_display().split(', '))
        self.assertEqual(book.get_categories_list(), book.get_categories_display().split(', '))

    def test_validate(self):
        book = Book.objects.get(id=1)
        Book._meta.get_field('tags').clean(['sex', 'work'], book)
        try:
            Book._meta.get_field('tags').clean(['sex1', 'work'], book)
            raise AssertionError()
        except ValidationError:
            pass

        Book._meta.get_field('categories').clean(['1', '2', '3'], book)
        try:
            Book._meta.get_field('categories').clean(['1', '2', '3', '4'], book)
            raise AssertionError()
        except ValidationError:
            pass
        try:
            Book._meta.get_field('categories').clean(['11', '12', '13'], book)
            raise AssertionError()
        except ValidationError:
            pass

    def test_serializer(self):
        book = Book.objects.get(id=1)
        self.assertEqual(Book._meta.get_field('tags').value_to_string(book), 'sex,work,happy')
        self.assertEqual(Book._meta.get_field('categories').value_to_string(book), '1,3,5')
