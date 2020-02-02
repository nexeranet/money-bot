from .views import frontend

def setup_routes(app):
    app.router.add_route('GET', '/', frontend.index)
    app.router.add_route('GET', '/her', frontend.index)
    app.router.add_route('GET', '/hex12', frontend.index)
    app.router.add_route('GET', '/hex12/', frontend.index2)
