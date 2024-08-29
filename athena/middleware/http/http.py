import time

from collections import defaultdict
from typing import Dict

from fastapi import status, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from athena.core import logger


class HTTPMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.rate_limit_records: Dict[str, float] = defaultdict(float)


    async def dispatch(self, request: Request, call_next) -> Response:
        client_ip = request.client.host
        path = request.url.path
        current_time = time.time()

        # Limit - 1 request per second
        if current_time - self.rate_limit_records[client_ip] < 1:
            logger.info(f'{client_ip} made too many requests to {path}')

            content = {
                'message': 'Too many requests made to the server. Please wait.'
            }

            return JSONResponse(
                content=content,
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            )

        self.rate_limit_records[client_ip] = current_time

        return await call_next(request)
