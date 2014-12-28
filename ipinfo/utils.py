#!/usr/bin/python
# -*- coding: utf-8 -*-
import re


def ip_list_from_string(string):
    return re.findall(r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+', string)
