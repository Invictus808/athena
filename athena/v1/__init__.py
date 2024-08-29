from fastapi import APIRouter

from .ping import *
from .website import *
from .red import *


# create router
router = APIRouter()


# add routers
router.include_router(ping.router, prefix='/ping', tags=['ping'])
router.include_router(website.router, prefix='/website', tags=['website'])
router.include_router(red.router, prefix='/red', tags=['red'])
