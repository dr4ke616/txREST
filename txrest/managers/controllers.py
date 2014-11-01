# -*- test-case-name: <INSERT_TEST_MODULE> -*-
# Copyright (c) 2014 Adam Drakeford <adam.drakeford@gmail.com>
# See LICENSE for more details

"""
.. module:: controller
    :platform: Linux
    :synopsis: The main routing manager for all the controllers.

.. moduleauthor:: Adam Drakeford <adam.drakeford@gmail.com>
"""

from collections import OrderedDict


class ControlManager(object):

    def __init__(self):

        self._controllers = OrderedDict()

    def __len__(self):

        return len(self._controllers)

    def install_controller(self, controller):

        self._controllers.update({
            controller.__route__: controller
        })

    def get_controllers(self):

        return self._controllers.values()

    def get_root_controller(self):

        if len(self) > 0:
            klass = self._controllers.itervalues().next()
            return klass.__class__.__bases__[0]()

    def build_controller_tree(self, controller):

        if controller.__parent__ is not None:
            parent = self._controllers.get(controller.__parent__)
            if parent is not None:
                parent.children[controller.__route__] = controller

    def get_full_route(self):
        pass
