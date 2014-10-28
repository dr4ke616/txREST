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

from twisted.web import server, resource
from twisted.application import service, internet


class BaseController(resource.Resource):

    def __init__(self):
        resource.Resource.__init__(self)

    def getChild(self, name, request):

        return self

    def render(self, request):

        request.write('Hello World!')
        return server.NOT_DONE_YET

    def run(self, port=8080):

        from twisted.internet import reactor

        factory = server.Site(self)
        reactor.listenTCP(port, factory)
        reactor.run()
