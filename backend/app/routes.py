from .views import frontend
from .controllers import webhook
from .bot.bot import Bot
from .bot.types.message import Message

bot = Bot()


@bot.register_handler(commands=['start', 'help'])
async def star_handler(message: Message):
    await message.send('Hi Oleh!)')


@bot.register_handler()
async def base_handler(message: Message):
    await message.send(message.get_text())


def setup_routes(app):
    app.router.add_route('GET', '/', frontend.index)
    app.router.add_route('GET', '/webhook', webhook.enterpoint)
    app.router.add_route('POST', '/webhook', bot.listen)
