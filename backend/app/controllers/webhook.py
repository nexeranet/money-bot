import json

from aiohttp.web import Response


async def enterpoint(request):
    print(request)
    return Response(content_type='application/json',
                    status=200,
                    text=json.dumps('webhook is ready')
                    )


async def test(request):
    return request


async def postWebhook(request):
    req = await request.json()
    print(req)
    if 'entities' in req.message:
        for en in req.message.entities:
            if en.command == 'bot_command':
                print(en)
    return Response(content_type='application/json',
                    status=200,
                    text=json.dumps('api is ready')
                    )
