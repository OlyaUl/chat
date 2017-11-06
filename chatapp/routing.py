# In routing.py
from channels.routing import route
from .consumers import ws_message

channel_routing = [
    route("http.request", "chatapp.consumers.http_consumer"),
    route("websocket.receive", ws_message),

]


'''from channels.routing import route


channel_routing = {
    route("http.request", "chatapp.views.consumer")
}


from channels.routing import route
from chatapp.consumers import ws_message

channel_routing = [
    route("websocket.receive", ws_message),
]'''