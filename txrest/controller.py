# -*- test-case-name: txrest.tests.test_controller.ControllerTest -*-
# Copyright (c) 2014 Adam Drakeford <adam.drakeford@gmail.com>
# See LICENSE for more details

"""
.. module:: controller
    :platform: Linux
    :synopsis: Controllers for web projects that encapsulates twisted
               low-level resources using custom routing system.

.. moduleauthor:: Adam Drakeford <adam.drakeford@gmail.com>
"""

from collections import defaultdict

from txrest.app import txREST

from twisted.web import server, resource


class ChildControllerManager(type):

    __inheritors__ = defaultdict(list)

    def __new__(meta, name, bases, dct):
        klass = type.__new__(meta, name, bases, dct)
        for base in klass.mro()[1:-1]:
            if base.__name__ == 'BaseController':
                meta.__inheritors__[base].append(klass)
        return klass


class NewStyleClass(object):
    """ In order to be able to automatically instanciate the controller
        objects using the ChildControllerManager meta_class the BaseController
        needs to be a New-Type class. Twisted's resource.Resource class is not
        a New-Type so we inherit from this class in our BaseController.

        In the future if this causes wierd behaviour we need to revisit this.
        To get around any possible problems dont inherit from this class,
        remove the `load_controllers` method call in the txREST object and
        instanciate each contoller manually
    """
    pass


class BaseController(NewStyleClass, resource.Resource):

    __parent__ = None
    __metaclass__ = ChildControllerManager

    _app = txREST()

    def __init__(self):
        resource.Resource.__init__(self)

        self._routing = self._app.managers.get('routes')
        self._controllers = self._app.managers.get('controllers')

        self._controllers.install_controller(self)

    def getChild(self, name, request):

        return self

    def get_path(self):

        try:
            return self.__route__
        except AttributeError:
            return ''

    def render(self, request):

        result = self._routing.execute_route(self, request)
        request.write(result)
        request.finish()

        return server.NOT_DONE_YET

    @property
    def full_url(self):

        return self._controllers.get_full_route(self)

    def run(self, port=8080):

        from twisted.internet import reactor

        factory = server.Site(self)
        reactor.listenTCP(port, factory)
        reactor.run()
