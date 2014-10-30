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

from routing import RouteManager

from twisted.web import server, resource
from twisted.application import service, internet


class BaseController(resource.Resource):

    _routing = RouteManager()

    def __init__(self):
        resource.Resource.__init__(self)
        self._routing.install_controller(self)

    def getChild(self, name, request):

        return self

    def render(self, request):

        env = {'REQUEST_METHOD': request.method, 'PATH_INFO': request.path}

        result = self._routing.execute_route(self, request)
        request.write(result)
        request.finish()

        return server.NOT_DONE_YET

    def run(self, port=8080):

        from twisted.internet import reactor

        factory = server.Site(self)
        reactor.listenTCP(port, factory)
        reactor.run()
