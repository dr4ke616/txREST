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

    def __init__(self):
        super(Unknown, self).__init__(209, '', {})


class BadRequest(Response):
    """ BadRequest 400 HTTP Response
    """

    def __init__(self, subject='', headers={}):
        super(BadRequest, self).__init__(http.BAD_REQUEST, subject, headers)


class Unauthorized(Response):
    """ Unauthorized 401 HTTP Response
    """

    def __init__(self, subject='Unauthorized', headers={}):
        super(Unauthorized, self).__init__(http.UNAUTHORIZED, subject, headers)


class Forbidden(Response):
    """ Forbidden 403 HTTP Response
    """

    def __init__(self, subject='Access is Forbidden', headers={}):
        super(Forbidden, self).__init__(http.FORBIDDEN, subject, headers)


class NotFound(Response):
    """ Not Found 404 HTTP Response
    """

    def __init__(self, subject='Not Found', headers={}):
        super(NotFound, self).__init__(http.NOT_FOUND, subject, headers)


class MovedPermanently(Response):
    """ Moved Permanently 301 HTTP Response
    """

    def __init__(self, url):
        super(MovedPermanently, self).__init__(
            http.MOVED_PERMANENTLY,
            '',
            {
                'content-type': 'text/plain; charset=utf-8',
                'location': url
            }
        )


class Found(Response):
    """ Found 302 HTTP Response
    """

    def __init__(self, url):
        super(Found, self).__init__(
            http.FOUND,
            '',
            {
                'content-type': 'text/plain; charset=utf-8',
                'location': url
            }
        )


class SeeOther(Response):
    """ See Other 303 HTTP Response
    """

    def __init__(self, url):
        super(SeeOther, self).__init__(
            http.SEE_OTHER,
            '',
            {
                'content-type': 'text/plain; charset=utf8',
                'location': url
            }
        )


class Conflict(Response):
    """ Conflict 409 HTTP Response
    """

    def __init__(self, subject, value, message=''):
        super(Conflict, self).__init__(
            http.CONFLICT,
            'Conflict for {subject} ({value}): {message}'.format(
                subject=subject,
                value=value,
                message=message
            ), {
                'x-subject': subject,
                'x-value': value
            }
        )


class AlreadyExists(Conflict):
    """ Conflict (Already Exists) 409 HTTP Response
    """

    def __init__(self, subject, value, message=''):
        super(AlreadyExists, self).__init__(
            subject,
            value,
            '{subject} already exists: {message}'.format(
                subject=subject,
                message=message
            )
        )


class InternalServerError(Response):
    """ Internal Server Error 500 HTTP Response
    """

    def __init__(self, message):
        super(InternalServerError, self).__init__(
            http.INTERNAL_SERVER_ERROR,
            message,
            {'content-type': 'text/plain'}
        )


class NotImplemented(Response):
    """ Not Implemented 501 HTTP Response
    """

    def __init__(self, url, message=''):
        super(NotImplemented, self).__init__(
            http.NOT_IMPLEMENTED,
            'Not Implemented: {url}\n{message}'.format(
                url=url, message=message
            ),
            {'content-type': 'text/plain'}
        )
