# -*- coding: utf-8 -*-

import sys


if sys.version_info[0] == 2:
    string = basestring
    string_type = unicode
else:
    string = str
    string_type = string


def get_max_length(choices, max_length, default=200):
    if max_length is None:
        if choices:
            return len(','.join([string_type(key) for key, label in choices]))
        else:
            return default
    return max_length
