# -*- test-case-name: txrest.tests.test_routes.RoutesTest -*-
# Copyright (c) 2014 Adam Drakeford <adam.drakeford@gmail.com>
# See LICENSE for more details

"""
.. module:: controller
    :platform: Linux
    :synopsis: The routing manger for the controllers.

.. moduleauthor:: Adam Drakeford <adam.drakeford@gmail.com>
"""

import routes
import inspect
import functools


class NotFound(Exception):
    pass


class Route(object):

    def __init__(self, url, method, callback):
        self.url = url
        self.method = method
        self.callback = callback


class RouteManager(object):

    def __init__(self):
        super(RouteManager, self).__init__()
        self._mapping = routes.Mapper()

    def install_routes(self, controller):

        for func in inspect.getmembers(
                controller, predicate=inspect.ismethod):
            if hasattr(func[1], 'route'):
                route = getattr(func[1], 'route')

                if type(route.method) in (tuple, list):
                    conditions = {'method': [m for m in route.method]}
                else:
                    conditions = {'method': [route.method]}

                url = '{}{}'.format(controller.full_url, route.url)
                self._mapping.connect(
                    None, url,
                    handler=route.callback,
                    conditions=conditions
                )

    def execute_route(self, controller, request):

        try:
            handler, kwargs = self._load_route_handler(request)
        except NotFound:
            return "NotFound"

        return handler(controller, request, **kwargs)

    def _load_route_handler(self, request):

        env = {'REQUEST_METHOD': request.method, 'PATH_INFO': request.path}
        match = self._mapping.match(environ=env)

        if match is None or match.get('handler') is None:
            raise NotFound

        handler = match.pop('handler')
        return handler, match

     # decorator
    def route(self, url, method='GET'):
        """Register routes for controllers or full REST resources.
        """

        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return func

            setattr(wrapper, 'route', Route(url, method, func))

            return wrapper

        return decorator
