from fastapi import APIRouter

from .connect import connect


# create router
router = APIRouter()


# GET ping
router.get('')(connect)


# export router
__all__ = [
    'router',
]
