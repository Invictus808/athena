from fastapi import APIRouter

from .about import about
from .contact import contact
from .experiences import experiences
from .hero import hero
from .projects import projects
from .skills import skills
from .socials import socials


# create router
router = APIRouter()


# GET
router.get('/hero')(hero)
router.get('/about')(about)
router.get('/experiences')(experiences)
router.get('/skills')(skills)
router.get('/projects')(projects)
router.get('/contact')(contact)
router.get('/socials')(socials)
