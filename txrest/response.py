# -*- test-case-name: <INSERT_TEST_MODULE> -*-
# Copyright (c) 2014 Adam Drakeford <adam.drakeford@gmail.com>
# See LICENSE for more details

"""
.. module:: controller
    :platform: Linux
    :synopsis: Response classes that can be envoked and returned back
        to the routing system

.. moduleauthor:: Adam Drakeford <adam.drakeford@gmail.com>
"""

from twisted.web import http


DEFAULT_HEADER_CONTENT_TYPE = u'text/plain; charset=utf-8'


class Response(object):
    """ Base class for all response types
    """

    def __init__(self, code, subject, headers):
        self.code = code
        self.subject = subject
        self.headers = headers


class Ok(Response):
    """ Ok 200 HTTP Response
    """

    def __init__(self, subject='', headers={}):
        super(Ok, self).__init__(http.OK, subject, headers)


class Created(Response):
    """ Created 201 HTTP Response
    """

    def __init__(self, subject='', headers={}):
        super(Created, self).__init__(http.CREATED, subject, headers)


class Unknown(Response):
    """ Unknown status 209 HTTP Response
    """

    def __init__(self, subject='', headers={}):
        super(Unknown, self).__init__(209, subject, headers)


class BadRequest(Response):
    """ BadRequest 400 HTTP Response
    """

    def __init__(self, subject='', headers={}):
        super(BadRequest, self).__init__(http.BAD_REQUEST, subject, headers)


class Unauthorized(Response):
    """ Unauthorized 401 HTTP Response
    """

    def __init__(self, subject='401: Unauthorized', headers={}):
        super(Unauthorized, self).__init__(http.UNAUTHORIZED, subject, headers)


class Forbidden(Response):
    """ Forbidden 403 HTTP Response
    """

    def __init__(self, subject='403: Access is Forbidden', headers={}):
        super(Forbidden, self).__init__(http.FORBIDDEN, subject, headers)


class NotFound(Response):
    """ Not Found 404 HTTP Response
    """

    def __init__(self, subject='404: Not Found', headers={}):
        super(NotFound, self).__init__(http.NOT_FOUND, subject, headers)


class MovedPermanently(Response):
    """ Moved Permanently 301 HTTP Response
    """

    def __init__(self, url, subject='', headers={}):
        if len(headers) == 0:
            headers = {
                'content-type': DEFAULT_HEADER_CONTENT_TYPE,
                'location': url
            }

        super(MovedPermanently, self).__init__(
            http.MOVED_PERMANENTLY, subject, headers
        )


class Found(Response):
    """ Found 302 HTTP Response
    """

    def __init__(self, url, subject='', headers={}):
        if len(headers) == 0:
            headers = {
                'content-type': DEFAULT_HEADER_CONTENT_TYPE,
                'location': url
            }

        super(Found, self).__init__(http.FOUND, subject, headers)


class SeeOther(Response):
    """ See Other 303 HTTP Response
    """

    def __init__(self, url, subject='', headers={}):
        if len(headers) == 0:
            headers = {
                'content-type': DEFAULT_HEADER_CONTENT_TYPE,
                'location': url
            }

        super(SeeOther, self).__init__(http.SEE_OTHER, subject, headers)


class Conflict(Response):
    """ Conflict 409 HTTP Response
    """

    def __init__(self, subject='', headers={}):
        super(Conflict, self).__init__(http.CONFLICT, subject, headers)


class InternalServerError(Response):
    """ Internal Server Error 500 HTTP Response
    """

    def __init__(self, subject='500: Internal Server Error', headers={}):
        if len(headers) == 0:
            headers = {'content-type': DEFAULT_HEADER_CONTENT_TYPE}

        super(InternalServerError, self).__init__(
            http.INTERNAL_SERVER_ERROR, subject, headers
        )


class NotImplemented(Response):
    """ Not Implemented 501 HTTP Response
    """

    def __init__(self, url, subject='', headers={}):
        if len(subject) == 0:
            subject = '501: Not Implemented: {}'.format(url)

        if len(headers) == 0:
            headers = {'content-type': DEFAULT_HEADER_CONTENT_TYPE}

        super(NotImplemented, self).__init__(
            http.NOT_IMPLEMENTED, subject, headers
        )
