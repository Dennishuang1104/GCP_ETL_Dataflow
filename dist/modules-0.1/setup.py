# -*- coding: utf-8 -*-
# coding:utf8
# coding=gbk
from setuptools import setup, find_packages

setup(
    name="modules",
    version="0.1",
    description="Repository",
    install_requires=['PyJWT~=2.3.0',
                      'google-cloud-logging==3.0.0',
                      'cryptography==36.0.1'],
    packages=find_packages(),
)