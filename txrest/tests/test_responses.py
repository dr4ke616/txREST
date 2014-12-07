# Copyright (c) 2014 Adam Drakeford <adam.drakeford@gmail.com>
# See LICENSE for more details

"""
Tests for txREST generic response classes
"""

from twisted.trial import unittest

from txrest.response import *


class ControllerTest(unittest.TestCase):
    """ Tests for txrest.controller
    """

    def setUp(self):
        self.subject = 'Test subject'
        self.headers = {'type': 'test'}

    def assert_response(self, response, code):
        self.assertEqual(response.code, code)
        self.assertEqual(response.subject, self.subject)
        self.assertEqual(response.headers, self.headers)

    def test_ok(self):
        response = Ok(subject=self.subject, headers=self.headers)
        self.assert_response(response, 200)

    def test_created(self):
        response = Created(subject=self.subject, headers=self.headers)
        self.assert_response(response, 201)

    def test_unknown(self):
        response = Unknown(subject=self.subject, headers=self.headers)
        self.assert_response(response, 209)

    def test_bad_request(self):
        response = BadRequest(subject=self.subject, headers=self.headers)
        self.assert_response(response, 400)

    def test_unauthorized(self):
        self.subject = '401: Unauthorized'
        response = Unauthorized(subject=self.subject, headers=self.headers)
        self.assert_response(response, 401)

    def test_forbidden(self):
        self.subject = '403: Access is Forbidden'
        response = Forbidden(subject=self.subject, headers=self.headers)
        self.assert_response(response, 403)

    def test_not_found(self):
        self.subject = '404: Not Found'
        response = NotFound(subject=self.subject, headers=self.headers)
        self.assert_response(response, 404)

    def test_moved_permanently(self):
        response = MovedPermanently('http://host.com/some/url')
        self.headers = response._get_default_header('http://host.com/some/url')
        self.subject = ''
        self.assert_response(response, 301)

    def test_moved_permanently_custom(self):
        self.headers = {'some_header': 'test header'}
        self.subject = ''
        response = MovedPermanently(
            'http://host.com/some/url', self.subject, self.headers
        )
        self.assert_response(response, 301)

    def test_found(self):
        response = Found('http://host.com/some/url')
        self.headers = response._get_default_header('http://host.com/some/url')
        self.subject = ''
        self.assert_response(response, 302)

    def test_moved_found_custom(self):
        self.headers = {'some_header': 'test header'}
        self.subject = ''
        response = Found(
            'http://host.com/some/url', self.subject, self.headers
        )
        self.assert_response(response, 302)

    def test_see_other(self):
        response = SeeOther('http://host.com/some/url')
        self.headers = response._get_default_header('http://host.com/some/url')
        self.subject = ''
        self.assert_response(response, 303)

    def test_see_other_custom(self):
        self.headers = {'some_header': 'test header'}
        self.subject = ''
        response = SeeOther(
            'http://host.com/some/url', self.subject, self.headers
        )
        self.assert_response(response, 303)

    def test_conflict(self):
        response = Conflict(subject=self.subject, headers=self.headers)
        self.assert_response(response, 409)

    def test_internal_server_error(self):
        response = InternalServerError()
        self.headers = response._get_default_header()
        self.subject = '500: Internal Server Error'
        self.assert_response(response, 500)

    def test_internal_server_error_custom(self):
        self.headers = {'some_header': 'test header'}
        self.subject = ''
        response = InternalServerError(self.subject, self.headers)
        self.assert_response(response, 500)

    def test_not_implemented(self):
        response = NotImplemented('http://host.com/some/url')
        self.headers = response._get_default_header('http://host.com/some/url')
        self.subject = '501: Not Implemented: http://host.com/some/url'
        self.assert_response(response, 501)

    def test_not_implemented_custom(self):
        self.headers = {'some_header': 'test header'}
        self.subject = 'My Test Subject'
        response = NotImplemented(
            'http://host.com/some/url', self.subject, self.headers
        )
        self.assert_response(response, 501)

