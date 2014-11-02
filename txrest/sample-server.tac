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

        return 'I am the parent'


class ChildController(controller.BaseController):

    __route__ = 'v1'
    __parent__ = 'api'

    @route('/my/{name}', method='GET')
    def test(self, request, **kwargs):

        return 'Hello {}, I am the child'.format(kwargs['name'])


# Run with
# twistd --nodaemon --python txrest/sample-server.tac

app.initialize()

txrest_service = app.start_webserver(port=8080)
application = service.Application('txREST App')
txrest_service.setServiceParent(application)
