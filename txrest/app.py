# -*- test-case-name: <INSERT_TEST_MODULE> -*-
# Copyright (c) 2014 Adam Drakeford <adam.drakeford@gmail.com>
# See LICENSE for more details

"""
.. module:: app
    :platform: Linux
    :synopsis: Main entry point for txREST.

.. moduleauthor:: Adam Drakeford <adam.drakeford@gmail.com>
"""

from twisted.web import server
from twisted.python import log
from twisted.application import service, internet

from txrest.utils.borg import Borg
from txrest.managers import controllers, routing


class txREST(Borg):

    def __init__(self):

        if hasattr(self, '_initialized') and self._initialized is True:
            return

        self.managers = {
            'routes': routing.RouteManager(),
            'controllers': controllers.ControlManager()
        }

        self._initialized = True

    def install_routes(self):

        route_manager = self.managers.get('routes')
        controller_manager = self.managers.get('controllers')

        for controller in controller_manager.get_controllers():
            route_manager.install_routes(controller)


def start_webserver(app, port=80):

    txrest_service = service.MultiService()
    txrest_service.setName('txREST')

    manager = app.managers.get('controllers')
    controller = manager.get_root_controller()
    if controller is None:
        log.err('You must have at least one controller initialized')
        return

    site = server.Site(controller)

    httpserver = internet.TCPServer(int(port), site)
    httpserver.setName('txREST Internal Server')
    httpserver.setServiceParent(txrest_service)

    return txrest_service


def initialize(start_server=False, port=8080):

    app = txREST()
    app.install_routes()

    if start_server:
        return start_webserver(app, port)

    return app
