import json


class Response:
    """Represents the outgoing HTTP response."""

    def __init__(self, send):
        self._status_code = 200  # Default status code
        self._body = b""  # Default body (empty byte string)
        self._content_type = "text/plain"  # Default content type (plain text)
        self._send = send

    def status(self, code: int):
        """Set the response status code."""
        self._status_code = code
        return self

    def send(
        self, status: int = None, message: any = "", content_type: str = "text/plain"
    ):
        """Send response with all custom params."""
        if status:
            self._status_code = status
        if content_type == "application/json":
            return self.json(message)

        return self.text(message)

    async def text(self, message: any):
        """Send plain text response."""
        self._body = str(message).encode()
        self._content_type = "text/plain"
        # TODO: Send instead of returning
        await self._send_response()

    async def json(self, message: any, status: int = None):
        """Send JSON response."""
        if status:
            self._status_code = status
        self._body = json.dumps(message).encode()
        self._content_type = "application/json"
        # TODO: Send instead of returning
        await self._send_response()

    async def _send_response(self):
        content_length = str(len(self._body)).encode()

        await self._send(
            {
                'type': 'http.response.start',
                'status': self._status_code,
                'headers': [
                    (b'content-type', self._content_type.encode()),
                    (b'content-length', content_length),
                ],
            }
        )
        await self._send(
            {
                'type': 'http.response.body',
                'body': self._body,
            }
        )
