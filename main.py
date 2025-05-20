import uvicorn

class App:
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

app = App()

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info", reload=True)
