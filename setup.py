#! /usr/bin/env python2.7
__author__ = "Adam Richardson"
__Date__ = 18 / 04 / 18

from setuptools import setup

setup(
    name='PalDB',
    packages=['PalDB'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)