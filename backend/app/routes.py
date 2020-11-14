from .views import frontend
from .controllers import webhook
from .telegram import Bot

bot = Bot()
def setup_routes(app):
    app.router.add_route('GET', '/', frontend.index)
    app.router.add_route('GET', '/webhook', webhook.enterpoint)
    app.router.add_route('POST', '/webhook', bot.setWebhook)
    # app.router.add_route('GET', '/hex12/', frontend.index2)
