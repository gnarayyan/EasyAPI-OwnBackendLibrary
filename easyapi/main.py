from easyapi.utils.exceptions import RouteAlreadyExistsError


class EasyAPI:
    def __init__(self):
        self.routes = dict()
    
    async def __call__(self, scope, receive, send):
        assert scope['type'] == 'http'
        
        print(f'Method: {scope["method"]}')
        print(f'Path: {scope["path"]}')

        body = b'Hello, world! from class based implementation'
        content_length = str(len(body)).encode()

        await send({
            'type': 'http.response.start',
            'status': 200,
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
                raise RouteAlreadyExistsError(f'GET {path_name} already registered')
        return wrapper
        