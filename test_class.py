# -*- test-case-name: <INSERT_TEST_MODULE> -*-
# Copyright (c) 2014 Adam Drakeford <adam.drakeford@gmail.com>
# See LICENSE for more details


from txrest import controller, route, app


class ParentController(controller.BaseController):

    __route__ = 'api'

    @route('/my/test/{name}/{age}', method='GET')
    def test(self, request, **kwargs):

        print kwargs['name']
        print kwargs['age']
        print 'i am here motha fucka'
        return 'Hello World'


class TestController(controller.BaseController):

    __parent__ = 'api'
    __route__ = 'v1'

    @route('/my/test/{name}/{age}', method='GET')
    def test(self, request, **kwargs):

        print kwargs['name']
        print kwargs['age']
        print 'i am here motha fucka'
        return 'Hello World'

    @route('/another/{pop}', method='GET')
    def another(self, request, pop):

        print pop
        return 'Another Hello1'

    @route('/another/{pop}', method='GET')
    def another(self, request, pop):

        print pop
        return 'Another Hello2'

class ChildController(controller.BaseController):

    __parent__ = 'api'
    __route__ = 'v2'

    @route('/my', method='GET')
    def test(self, request, **kwargs):

        print 'i am here motha fucka'


class PopController(controller.BaseController):

    __parent__ = 'v1'
    __route__ = 'test'

    @route('/pop', method='GET')
    def pop(self, request, **kwargs):

        print 'Poop'
        return 'Hello World'

def main():

    PopController()
    ChildController()
    ParentController()

    controller = TestController()
    app.initialize()
    controller.run()


if __name__ == '__main__':
    main()
