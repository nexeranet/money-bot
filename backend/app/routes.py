from .views import frontend
from .controllers import webhook

def setup_routes(app):
    app.router.add_route('GET', '/', frontend.index)
    app.router.add_route('GET', '/webhook', webhook.enterpoint)
    # app.router.add_route('GET', '/hex12/', frontend.index2)
