# -*- coding: utf-8 -*-

import sys

import django

from django.db import models
from django.utils.text import capfirst
from django.core import exceptions

from ..forms.fields import MultipleSelectionFormField, MaxChoicesValidator
from ..utils import get_max_length
from ..validators import MaxValueMultiFieldValidator

string_type = str

# Code from six egg https://bitbucket.org/gutworth/six/src/a3641cb211cc360848f1e2dd92e9ae6cd1de55dd/six.py?at=default


class MultipleSelectionField(models.CharField):
    """ Choice values can not contain commas. """

    def __init__(self, *args, **kwargs):
        self.max_choices = kwargs.pop('max_choices', None)
        super(MultipleSelectionField, self).__init__(*args, **kwargs, validators=())
        self.max_length = get_max_length(self.choices, self.max_length)
        self.validators.insert(0, MaxValueMultiFieldValidator(self.max_length))
        if self.max_choices is not None:
            self.validators.append(MaxChoicesValidator(self.max_choices))

    @property
    def flatchoices(self):
        return None

    def get_choices_default(self):
        return self.get_choices(include_blank=False)

    def get_choices_selected(self, arr_choices):
        choices_selected = []
        for choice_selected in arr_choices:
            choices_selected.append(string_type(choice_selected[0]))
        return choices_selected

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)

    def validate(self, value, model_instance):
        arr_choices = self.get_choices_selected(self.get_choices_default())
        for opt_select in value:
            if (opt_select not in arr_choices):
                raise exceptions.ValidationError(self.error_messages['invalid_choice'] % {"value": value})

    def get_default(self):
        default = super(MultipleSelectionField, self).get_default()
        if isinstance(default, int):
            default = string_type(default)
        if isinstance(default, string_type):
            default = default.split(',')
        return default

    def formfield(self, **kwargs):
        defaults = {'required': not self.blank,
                    'label': capfirst(self.verbose_name),
                    'help_text': self.help_text,
                    'choices': self.choices,
                    'max_length': self.max_length,
                    'max_choices': self.max_choices}
        if self.has_default():
            defaults['initial'] = self.get_default()
        defaults.update(kwargs)
        return MultipleSelectionFormField(**defaults)

    def get_prep_value(self, value):
        return '' if value is None else ",".join(value)

    def to_python(self, value):
        if value:
            return value if isinstance(value, (list, set)) else value.split(',')
        return []

    if django.VERSION < (2,):
        def from_db_value(self, value, expression, connection, context):
            return self.to_python(value)
    else:
        def from_db_value(self, value, expression, connection):
            return self.to_python(value)

    def contribute_to_class(self, cls, name):
        super(MultipleSelectionField, self).contribute_to_class(cls, name)
        if self.choices:
            def get_list(obj):
                fieldname = name
                choicedict = dict(self.choices)
                display = []
                if getattr(obj, fieldname):
                    for value in getattr(obj, fieldname):
                        item_display = choicedict.get(value, None)
                        if item_display is None:
                            try:
                                item_display = choicedict.get(int(value), value)
                            except (ValueError, TypeError):
                                item_display = value
                        display.append(string_type(item_display))
                return display

            def get_display(obj):
                return ", ".join(get_list(obj))

            setattr(cls, 'get_%s_list' % self.name, get_list)
            setattr(cls, 'get_%s_display' % self.name, get_display)


try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ['^multipleselectionfield\.db.fields\.MultipleSelectionField'])
except ImportError:
    pass
