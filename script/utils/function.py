#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from collections import defaultdict as dd


def open_json(path):
    """Return variable contained in a json file."""
    with open(path) as data_file:
        return json.load(data_file)


def create_json(path, var):
    """Create a json file to the indicate path."""
    with open(path, 'w+') as stream:
        json.dump(var, stream)  # , indent=2, sort_keys=True)


def dic_to_default(dic):
    """Transform a dict to a defaultdict."""
    data = dd(str)
    for key in dic.keys():
        data[key] = dic[key]
    return data
