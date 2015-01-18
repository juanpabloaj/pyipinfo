#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from ipinfo.utils import ip_list_from_string


class TestUtils(unittest.TestCase):

    def test_ip_from_string(self):
        string_with_ips = 'abc 10.10.10.10 cde 20.20.20.20'
        ip_list = ['10.10.10.10', '20.20.20.20']

        self.assertItemsEqual(ip_list_from_string(string_with_ips), ip_list)

    def test_ip_from_string_without_ips(self):
        string_with_ips = 'string without ip'

        self.assertItemsEqual(ip_list_from_string(string_with_ips), [])
