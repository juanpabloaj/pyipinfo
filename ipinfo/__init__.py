#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import sys
from ipinfo.utils import ip_list_from_string
from ipinfo.utils import is_piped


def request_to_ipinfo(ip):
    ''' return a json from the request '''
    full_url = 'http://ipinfo.io/{}'.format(ip)
    headers = {'User-Agent': 'curl/7.30.0'}
    req = requests.get(full_url, headers=headers)
    if req.status_code == 200:
        return req.json()


def main():

    if is_piped():
        input_string = sys.stdin.read()
        ip_list = ip_list_from_string(input_string)
    else:
        ip_list = ['']

    if ip_list == []:
        exit()

    ip_set = set(ip_list)

    ips_info = []
    for ip in ip_set:
        ips_info.append(request_to_ipinfo(ip))

    all_keys = [
        'ip', 'city', 'region', 'country',
        'hostname', 'org', 'postal', 'loc'
    ]

    for info in ips_info:
        for k in all_keys:
            try:
                print '{}\t'.format(info[k]),
            except KeyError:
                print '\t',
        print


if __name__ == '__main__':
    main()
