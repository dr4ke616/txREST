# Copyright (c) 2014 Adam Drakeford <adam.drakeford@gmail.com>
# See LICENSE for more details

"""
Tests for txREST controllers
"""

import routes

from twisted.trial import unittest
from twisted.internet import defer

from txrest import route
from txrest.managers.routing import RouteManager, NotFound
from txrest.tests.helpers import MockController, MockRequest


class Dummy(MockController):
    full_url = '/v1/api/some/url'

    @route('/', method='GET')
    def test_one(self, request, **kwargs):
        return 'I am root'

    @route('/endpoint1', method=['GET', 'POST'])
    def test_two(self, request, **kwargs):
        return 'I am endpoint1'

    @route('/endpoint2/{arg1}', method='GET')
    def test_three(self, request, arg1, **kwargs):
        return 'I am endpoint2 with {}'.format(arg1)


class RoutesTest(unittest.TestCase):
    """ Tests for txrest.controller
    """

    def setUp(self):
        self.r = RouteManager()

    def install_route(self):
        controller = Dummy()
        self.r.install_routes(controller)
        self.assertIsInstance(self.r._mapping, routes.Mapper)
        return controller

    def test_install_route(self):
        self.install_route()

        env = {'REQUEST_METHOD': 'GET', 'PATH_INFO': '/v1/api/some/url/'}
        match = self.r._mapping.match(environ=env)
        self.assertIsInstance(match, dict)
        self.assertTrue(hasattr(match['handler'], '__call__'))
        self.assertEqual(match['handler'].__name__, 'test_one')

        env = {
            'REQUEST_METHOD': 'POST',
            'PATH_INFO': '/v1/api/some/url/endpoint1'
        }
        match = self.r._mapping.match(environ=env)
        self.assertIsInstance(match, dict)
        self.assertTrue(hasattr(match['handler'], '__call__'))
        self.assertEqual(match['handler'].__name__, 'test_two')

    def test_lookup_route(self):
        self.install_route()

        req = MockRequest()
        req.method = 'GET'
        req.path = '/v1/api/some/url/'

        func, _ = self.r._load_route_handler(req)
        self.assertTrue(func, '__call__')
        self.assertEqual(func.__name__, 'test_one')

        req.method = 'POST'
        req.path = '/v1/api/some/url/endpoint1'

        func, _ = self.r._load_route_handler(req)
        self.assertTrue(func, '__call__')
        self.assertEqual(func.__name__, 'test_two')

    def test_lookup_route_with_args(self):
        self.install_route()

        req = MockRequest()
        req.method = 'GET'
        req.path = '/v1/api/some/url/endpoint2/test_arg'

        func, _ = self.r._load_route_handler(req)
        self.assertTrue(func, '__call__')
        self.assertEqual(func.__name__, 'test_three')

    @defer.inlineCallbacks
    def test_execute_route(self):
        c = self.install_route()

        req = MockRequest()
        req.method = 'GET'
        req.path = '/v1/api/some/url/'

        retval = yield self.r.execute_route(c, req)
        self.assertEqual(retval, 'I am root')

    @defer.inlineCallbacks
    def test_execute_route_with_args(self):
        c = self.install_route()

        req = MockRequest()
        req.method = 'GET'
        req.path = '/v1/api/some/url/endpoint2/test_arg'

        retval = yield self.r.execute_route(c, req)
        self.assertEqual(retval, 'I am endpoint2 with test_arg')

    @defer.inlineCallbacks
    def test_execute_route_not_found(self):
        c = self.install_route()

        req = MockRequest()
        req.method = 'GET'
        req.path = '/v1/api'

        retval = yield self.r.execute_route(c, req)
        self.assertEqual(retval, 'NotFound')

    def test_not_found_route_on_method(self):
        self.install_route()

        req = MockRequest()
        req.method = 'PATCH'
        req.path = '/v1/api/some/url/'

        retval = self.r._load_route_handler(req)
        self.assertEqual(retval[0], 'NotFound')

    def test_not_found_route_on_url(self):
        self.install_route()

        req = MockRequest()
        req.method = 'GET'
        req.path = '/v1/api/some/url/doesnt/exist'

        retval = self.r._load_route_handler(req)
        self.assertEqual(retval[0], 'NotFound')

    def test_not_found_route_on_both(self):
        self.install_route()

        req = MockRequest()
        req.method = 'DELETE'
        req.path = '/v1/api/some/url/doesnt/exist'

        retval = self.r._load_route_handler(req)
        self.assertEqual(retval[0], 'NotFound')
