# -*- coding: utf-8 -*-


from django.core import validators
from django.utils.translation import ugettext_lazy as _


class MaxValueMultiFieldValidator(validators.MaxLengthValidator):
    clean = lambda self, x: len(','.join(x))
    code = 'max_multifield_value'


class MaxChoicesValidator(validators.MaxLengthValidator):
    message = _(u'You must select a maximum of  %(limit_value)d choices.')
    code = 'max_choices'
