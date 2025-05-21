from easyapi.utils.exceptions import RouteError
from urllib.parse import parse_qs

class EasyAPI:
    def __init__(self):
        self.routes = dict()
    
    async def __call__(self, scope, receive, send):
        response = {}
        status_code = 200
        message = 'Hello, world! from class based implementation'
        # print(f'****\n\nScope: {scope} \n\n Receive: {receive}  \n\n Send: {send}\n\n *****\n\n')
        assert scope['type'] == 'http'
        path = scope["path"] # Like /users
        method = scope["method"] # Like get
        query_string = scope.get('query_string', b'')
        query_params = parse_qs(query_string.decode())
        print(f'Query Params: {query_params}')
        
        if self.routes.get(path):
            if self.routes[path].get(method):
                handler = self.routes[path][method] 
                message = handler()
            else:
                status_code = 404
                message = f'Method {method} isn\'t registered in path {path}'
        else:
            status_code = 404
            message = f'Path {path} isn\'t registered'

        await self._sendTextResponse(send, status_code, message)
    
    async def _sendTextResponse(self, send,status_code:int,message:str ):

        body = str(message).encode()
        content_length = str(len(message)).encode()

        await send({
            'type': 'http.response.start',
            'status': status_code,
            'headers': [
                (b'content-type', b'text/plain'),
                (b'content-length', content_length),
            ],
        })
        await send({
            'type': 'http.response.body',
            'body': body,
        })

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
        