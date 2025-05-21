from easyapi.utils.request import Request
from easyapi.utils.response import Response
from easyapi.utils.exceptions import RouteError

# from urllib.parse import parse_qs
# import json


class EasyAPI:
    def __init__(self):
        self._routes = dict()

    async def __call__(self, scope, receive, send):
        """Handle the request and response."""
        request = Request(scope, receive)
        response = Response(send=send)

        assert scope['type'] == 'http'
        path = scope["path"]  # Like /users
        method = scope["method"]  # Like get
        # query_string = scope.get('query_string', b'')
        # query_params = parse_qs(query_string.decode())
        # print(f'Query Params: {query_params}')

        if self._routes.get(path):
            if self._routes[path].get(method):
                handler = self._routes[path][method]
                await handler(request, response)
            else:
                await response.status(404).json(
                    f'Method {method} isn\'t registered in path {path}'
                )

        else:
            await response.status(404).json(f'Path {path} isn\'t registered')

    def get(self, path=None):
        def wrapper(handler):
            return self._http_wrapper(handler=handler, method_name='GET', path=path)

        return wrapper

    def post(self, path=None):
        def wrapper(handler):
            return self._http_wrapper(handler=handler, method_name='POST', path=path)

        return wrapper

    def patch(self, path=None):
        def wrapper(handler):
            return self._http_wrapper(handler=handler, method_name='PATCH', path=path)

        return wrapper

    def put(self, path=None):
        def wrapper(handler):
            return self._http_wrapper(handler=handler, method_name='PUT', path=path)

        return wrapper

    def delete(self, path=None):
        def wrapper(handler):
            return self._http_wrapper(handler=handler, method_name='DELETE', path=path)

        return wrapper

    def _http_wrapper(self, handler, method_name, path=None):
        path_name = path or ''
        if path_name not in self._routes:
            self._routes[path_name] = {}

        if method_name not in self._routes[path_name]:
            self._routes[path_name][method_name] = handler
            print(f'GET  {path_name} Registered')
        else:
            raise RouteError(f'{method_name} {path_name} already registered')
