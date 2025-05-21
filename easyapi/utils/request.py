import json


class Request:
    """Represents the incoming HTTP request."""

    def __init__(self, scope, receive):
        self._scope = scope  # Will be used later for parsing query string
        self._receive = receive
        self.body = None

    async def initialize(self):
        """Asynchronous initialization of the request, reads the body."""
        self.body = await self._parse_body()

    async def _parse_body(self):
        """Read and return the entire body from an incoming ASGI message."""
        body = b''
        more_body = True

        while more_body:
            message = await self._receive()
            body += message.get('body', b'')
            more_body = message.get('more_body', False)

        # Decode the byte string to a normal string
        body_str = body.decode('utf-8')

        # Parse the string as JSON (convert to a Python dictionary)
        try:
            return json.loads(body_str)
        except json.JSONDecodeError:
            return None  # If JSON decoding fails, set it to None
