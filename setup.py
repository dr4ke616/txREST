#!/usr/bin/env python
# Copyright (c) 2014 Adam Drakeford <adam.drakeford@gmail.com>
# See LICENSE for more details

"""
Distutils installer for txREST.
"""

from setuptools import setup, find_packages

setup(
    name='txREST',
    version='1.0',
    description=(
        'Inspired by the routing system of Mamba and the simplicity of Flask '
        'txREST is a fully REST compliant asynchronous micro framework using '
        'Twisted. '),
    author='Adam Drakeford',
    author_email='adam.drakeford@gmail.com',
    license='MIT',
    packages=find_packages(),
    tests_require=['twisted>=10.2.0', 'routes'],
    install_requires=['twisted>=10.2.0', 'routes'],
    requires=['twisted(>=10.2.0)', 'routes'],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Twisted',
        'Intended Audience :: Developers',
        'License :: MIT License (MIT)',
        'Operating System :: POSIX :: Linux',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: System :: Networking',
    ],
)
