class Request:
    """Represents the incoming HTTP request."""

    def __init__(self, scope, receive):
        self.scope = scope # Will be used later for parsing query string
        self.receive = receive

    async def get_body(self):
        """Read and return the entire body from an incoming ASGI message."""
        body = b''
        more_body = True

        while more_body:
            message = await self.receive()
            body += message.get('body', b'')
            more_body = message.get('more_body', False)

        return body