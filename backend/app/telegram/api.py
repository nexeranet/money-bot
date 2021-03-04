import json
from aiohttp.web import Response


class Bot:
    """
    Base bot class
    """

    async def setWebhook(self, request):
        req = await request.json()
        if 'entities' in req['message']:
            for en in req['message']['entities']:
                print(en)
                if en['type'] == 'bot_command':
                    print(en['type'])

        return Response(content_type='application/json',

                        status=200,
                        text=json.dumps(req['message'])
                        )
