import json
import os
from aiohttp.web import Response
import requests


TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_API = f"https://api.telegram.org/bot{TOKEN}/"


class Bot:
    """
    Base bot class
    """

    def get_url(self, module):
        return f"{TELEGRAM_API}{module}"

    async def sendMessage(self, chat_id, text):
        url = self.get_url('sendMessage')
        answer = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        return requests.post(url, json=answer)

    async def listen(self, request):
        req = await request.json()
        print(req)
        if 'entities' in req['message']:
            for en in req['message']['entities']:
                print(en)
                if en['type'] == 'bot_command':
                    print(en['type'])
        await self.sendMessage(req['message']['chat']['id'],
                               req['message']['text'])
        return Response(content_type='application/json',
                        status=200,
                        text=json.dumps(req['message'])
                        )
