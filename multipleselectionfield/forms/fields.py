# -*- coding: utf-8 -*-

from django import forms

from ..utils import get_max_length
from ..validators import MaxValueMultiFieldValidator, MaxChoicesValidator


class MultipleSelectionFormField(forms.MultipleChoiceField):
    widget = forms.CheckboxSelectMultiple

    def __init__(self, *args, **kwargs):
        self.max_choices = kwargs.pop('max_choices', None)
        self.max_length = kwargs.pop('max_length', None)
        super(MultipleSelectionFormField, self).__init__(*args, **kwargs)
        self.max_length = get_max_length(self.choices, self.max_length)
        self.validators.append(MaxValueMultiFieldValidator(self.max_length))
        if self.max_choices is not None:
            self.validators.append(MaxChoicesValidator(self.max_choices))
