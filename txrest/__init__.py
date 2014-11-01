# -*- test-case-name: <INSERT_TEST_MODULE> -*-
# Copyright (c) 2014 Adam Drakeford <adam.drakeford@gmail.com>
# See LICENSE for more details

"""
.. module:: controller
    :platform: Linux
    :synopsis: Just the __init__.py file

.. moduleauthor:: Adam Drakeford <adam.drakeford@gmail.com>
"""

from txrest.managers.routing import RouteManager


route = RouteManager().route
