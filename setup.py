#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from setuptools import setup


def read(*paths):
    """ read files """
    with open(os.path.join(*paths), 'r') as filename:
        return filename.read()


setup(
    name="pyipinfo",
    version="0.1.0",
    description="ipinfo.io in the command line",
    long_description=(read('README.rst')),
    url="https://github.com/juanpabloaj/pyipinfo",
    install_requires=['requests==2.5.1'],
    license='MIT',
    author="JuanPablo AJ",
    author_email="jpabloaj@gmail.com",
    packages=['ipinfo'],
    test_suite="tests",
    entry_points={
        'console_scripts': [
            'ipinfo=ipinfo:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 2.7'
    ]
)
