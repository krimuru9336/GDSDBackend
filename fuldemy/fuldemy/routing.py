from channels.routing import ProtocolTypeRouter, URLRouter

from AllUsers.channelsmiddleware import TokenAuthMiddleware
from AllUsers import routing as core_routing

application = ProtocolTypeRouter({
    "websocket": TokenAuthMiddleware(
        URLRouter(
            core_routing.websocket_urlpatterns
        )
    ),
})
