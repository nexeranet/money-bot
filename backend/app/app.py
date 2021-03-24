
from aiohttp import web
import jinja2
import aiohttp_jinja2
from .routes import setup_routes
from .db import *


async def create_app():
    app = web.Application()
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.PackageLoader('app', 'templates'),
    )
    setup_routes(app)
    return app
