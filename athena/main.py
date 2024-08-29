from fastapi import FastAPI

import athena

from athena.core import logger
from athena.middleware import HTTPMiddleware


# create api
logger.debug('Instantiating ATHENA...')
app = FastAPI()
logger.debug('Instantiated ATHENA.')

# add api router
logger.debug('Adding routers...')
app.include_router(athena.router)
logger.debug('Added routers.')

# add middleware
logger.debug('Adding middleware...')
app.add_middleware(HTTPMiddleware)
logger.debug('Added middleware.')
