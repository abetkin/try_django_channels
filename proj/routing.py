from django.conf.urls import url

from channels.routing import ProtocolTypeRouter, URLRouter

from app.consumers import MyConsumer

application = ProtocolTypeRouter({

    # WebSocket chat handler
    "websocket": URLRouter([
        url("^ws$", MyConsumer),
    ]),

})