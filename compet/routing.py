from django.core.asgi import get_asgi_application

import WebSocket.routing

django_asgi_app = get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(WebSocket.routing.websocket_urlpatterns)
    ),
})
