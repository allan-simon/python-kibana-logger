#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
setup tools
'''

from setuptools import setup, find_packages

setup(
    name='kibana-logger',
    version=":versiontools:kibana_logger:",
    description="module to simply log in syslog with CEE/json format for analysing by kibana",
    long_description="",
    keywords='kibana, syslog, cee, json',
    author='Allan SIMON',
    author_email='allan.simon@supinfo.com',
    url='https://github.com/allan-simon/python-kibana-logger',
    license='MIT',
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python",
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    setup_requires=[
        'versiontools >= 1.8',
    ],
)
