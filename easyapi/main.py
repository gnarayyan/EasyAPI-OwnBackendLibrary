from easyapi.utils.request import Request
from easyapi.utils.response import Response
from easyapi.utils.exceptions import RouteError

# from urllib.parse import parse_qs
# import json


class EasyAPI:
    def __init__(self):
        self.routes = dict()

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

        if self.routes.get(path):
            if self.routes[path].get(method):
                handler = self.routes[path][method]
                await handler(request, response)
            else:
                await response.status(404).json(
                    f'Method {method} isn\'t registered in path {path}'
                )

        else:
            await response.status(404).json(f'Path {path} isn\'t registered')

    def get(self, path=None):
        def wrapper(handler):
            path_name = path or ''
            if path_name not in self.routes:
                self.routes[path_name] = {}

            if 'GET' not in self.routes[path_name]:
                self.routes[path_name]['GET'] = handler
                print(f'GET  {path_name} Registered')
            else:
                raise RouteError(f'GET {path_name} already registered')

        return wrapper
