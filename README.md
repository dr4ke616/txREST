# txREST

[![Build Status](https://travis-ci.org/dr4ke616/txREST.svg?branch=master)](https://travis-ci.org/dr4ke616/txREST)

Inspired by the routing system of [Mamba](http://www.pymamba.com/) and the simplicity of [Flask](http://flask.pocoo.org/) ```txREST``` is a fully REST compliant asynchronous micro framework using [Twisted](http://twistedmatrix.com).
Note: This project is stil under development.

<!-- ## Installation

```shell
pip install txrest
```
 -->

## Usage
Routes are handled a bit differently than Flask and Mamba, in that they use the [routes](https://github.com/bbangert/routes) library.  A controller that is inherited from ```txREST``` base controller is just a sub class of [twisted.web.resource.Resource](http://twistedmatrix.com/documents/current/api/twisted.web.resource.Resource.html).

```python
from txrest import controller, route

class ParentController(controller.BaseController):

    __route__ = 'api'

    @route('/', method='GET')
    def test(self, request, **kwargs):

        return 'I am the parent'
```

You can also use the routing system to create sub-urls. Making versioning of APIs very easy. For example: ```http://host/api/v1/defer``` can be easily updated to ```http://host/api/v2/endpoint```.

```python
from txrest import controller, route

class ChildControllerVersionOne(controller.BaseController):

    __route__ = 'v1'
    __parent__ = 'api'

    @route('/my/{name}', method='GET')
    def test(self, request, **kwargs):

        return 'Hello {}, I am the child'.format(kwargs['name'])

    @route('/defer', method='GET')
    def test_defer(self, request, **kwargs):

        d = defer.succeed('I am the defered child')
        return d

class ChildControllerVersionTwo(controller.BaseController):

    __route__ = 'v2'
    __parent__ = 'api'

    @route('/endpoint}', method='GET')
    def test(self, request, **kwargs):

        return 'Hello {}, I am the child'.format(kwargs['name'])
```

As you can see, defers can also be handled.

You can use Twisted's built in webserver to start the application, or just import your controller classes to any other Twisted project. You need to initialize ```txREST``` somewhere in your project or in a Twisted tac file.

```python
from txrest import app

app.initialize()

txrest_service = app.start_webserver(port=8080)
application = service.Application('txREST App')
txrest_service.setServiceParent(application)
```

To startup the webserver execute the Twisted tac file using something like ```twistd --nodaemon --python txrest/sample-server.tac```.
