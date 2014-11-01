# -*- test-case-name: <INSERT_TEST_MODULE> -*-
# Copyright (c) 2014 Adam Drakeford <adam.drakeford@gmail.com>
# See LICENSE for more details

"""
.. module:: app
    :platform: Linux
    :synopsis: Main entry point for txREST.

.. moduleauthor:: Adam Drakeford <adam.drakeford@gmail.com>
"""

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


def initialize():

    app = txREST()

    manager = app.managers.get('controllers')
    for controller in manager.get_controllers():
        manager.build_controller_tree(controller)

    return app
