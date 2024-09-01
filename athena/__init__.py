from fastapi import APIRouter

from athena import v1 #, v2, ...


# create router
router = APIRouter()

# add routers
router.include_router(v1.router, prefix='/v1', tags=['v1'])


# export router
__all__ = [
    'router',
]
