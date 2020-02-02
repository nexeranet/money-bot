import aiohttp
from aiohttp_jinja2 import template

@template('index.html')
async def index(request):
    return {}

@template('index2.html')
async def index2(request):
    return {}
