# -*- test-case-name: <INSERT_TEST_MODULE> -*-
# Copyright (c) 2014 Adam Drakeford <adam.drakeford@gmail.com>
# See LICENSE for more details

"""
.. module:: controller
    :platform: Linux
    :synopsis: Simple Tac file to get things started.

.. moduleauthor:: Adam Drakeford <adam.drakeford@gmail.com>
"""

from twisted.application import service

from txrest import controller, route, app


class ParentController(controller.BaseController):

    __route__ = 'api'

    @route('/', method='GET')
    def test(self, request, **kwargs):

        return 'Hello World'


# Run with
# twistd --nodaemon --python txrest/run-server.tac

ParentController()

txrest_service = app.initialize(start_server=True)
application = service.Application('txREST App')
txrest_service.setServiceParent(application)

