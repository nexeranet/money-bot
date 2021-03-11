import json
import os
import aiohttp
import asyncio
from typing import Optional
from aiohttp.web import Response
from .handlers.handlers import Handlers
from .types.message import Message


TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_API = f"https://api.telegram.org/bot{TOKEN}/"


class NetworkError(Exception):
    pass


class Bot:
    """Base bot class."""

    def __init__(self):
        self.handlers = Handlers(self)
        self._session: Optional[aiohttp.ClientSession] = None

    def get_new_session(self) -> aiohttp.ClientSession:
        return aiohttp.ClientSession()

    @property
    def session(self) -> Optional[aiohttp.ClientSession]:
        if self._session is None or self._session.closed:
            self._session = self.get_new_session()
        return self._session

    def get_url(self, module):
        """ get telegram bot url

        Args:
            module: string module telegram api
        """
        return f"{TELEGRAM_API}{module}"

    def compose_data(self, params=None):
        data = aiohttp.formdata.FormData(quote_fields=False)
        if params:
            for key, value in params.items():
                data.add_field(key, str(value))
        return data

    async def make_request(self, session, method, data=None):
        url = self.get_url(method)
        compose = self.compose_data(data)

        try:
            async with session.post(url, data=compose) as response:
                return await response.text()
        except aiohttp.ClientError as e:
            raise NetworkError(f"NetworkError:{e.__class__.__name__}: {e}")

    async def sendMessage(self, chat_id, text):
        """Send message to user.

        Args:
            chat_id: chat id user
            text: bot message
        """
        # url = self.get_url('sendMessage')
        answer = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        return await self.make_request(self.session, 'sendMessage',
                                       data=answer)
        # return requests.post(url, json=answer)

    def register_handler(self, commands=None, regexp=None, content_type=None,
                         state=None):
        def decorator(callback):
            self.handlers.register(callback, commands=commands, regexp=regexp)
            return callback
        return decorator

    async def listen(self, request):
        req = await request.json()
        message = Message(content=req['message'], bot=self)
        await self.handlers.notify(message=message)
        await self.sendMessage(req['message']['chat']['id'],
                               req['message']['text'])
        return Response(content_type='application/json',
                        status=200,
                        text=json.dumps(req['message'])
                        )
