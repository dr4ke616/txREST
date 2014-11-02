# Copyright (c) 2014 Adam Drakeford <adam.drakeford@gmail.com>
# See LICENSE for more details

"""
Helper mock classes goes here
"""


class MockBaseController(object):

    __parent__ = None

    def get_path(self):

        try:
            return self.__route__
        except AttributeError:
            return ''


class MockController(MockBaseController):

    __route__ = 'api'


class MockControllerChildOne(MockBaseController):

    __route__ = 'v1'
    __parent__ = 'api'


class MockControllerChildTwo(MockBaseController):

    __route__ = 'v2'
    __parent__ = 'api'


class MockControllerSubChildOne(MockBaseController):

    __route__ = 'test1'
    __parent__ = 'v1'


class MockControllerSubChildTwo(MockBaseController):

    __route__ = 'test2'
    __parent__ = 'v2'


class MockRequest(object):

    method = 'GET'
    path = '/v1/api/some/url'
