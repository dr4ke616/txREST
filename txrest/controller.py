# -*- test-case-name: <INSERT_TEST_MODULE> -*-
# Copyright (c) 2014 Adam Drakeford <adam.drakeford@gmail.com>
# See LICENSE for more details

"""
.. module:: controller
    :platform: Linux
    :synopsis: Controllers for web projects that encapsulates twisted
               low-level resources using custom routing system.

.. moduleauthor:: Adam Drakeford <adam.drakeford@gmail.com>
"""

import inspect
from collections import OrderedDict

from txrest.app import txREST

from twisted.web import server, resource
from twisted.application import service, internet


class BaseController(resource.Resource):

    __route__ = '/'
    __parent__ = None

    _app = txREST()

    children = OrderedDict()

    def __init__(self):
        resource.Resource.__init__(self)

        self._routing = self._app.managers.get('routes')
        self._controllers = self._app.managers.get('controllers')

        self._routing.install_routes(self)
        self._controllers.install_controller(self)

    def getChild(self, name, request):

        return self

    def render(self, request):

        result = self._routing.execute_route(self, request)
        request.write(result)
        request.finish()

        return server.NOT_DONE_YET

    def run(self, port=8080):

        from twisted.internet import reactor

        factory = server.Site(self)
        reactor.listenTCP(port, factory)
        reactor.run()
