class EasyAPI:
    async def __call__(self, scope, receive, send):
        assert scope['type'] == 'http'

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

