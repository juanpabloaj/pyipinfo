# -*- coding: utf-8 -*-
from __future__ import absolute_import
import re
import os
import stat


def ip_list_from_string(string):
    return re.findall(r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+', string)


def is_piped():
    '''
        script is called from a pipe
        echo ip | ipinfo
    '''
    mode = os.fstat(0).st_mode
    return stat.S_ISFIFO(mode)
