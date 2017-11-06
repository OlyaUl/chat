# In routing.py
from channels.routing import route
from .consumers import ws_message, ws_add, ws_disconnect

channel_routing = [
    # route("http.request", "chatapp.consumers.http_consumer"),
    route("websocket.receive", ws_message),
    route("websocket.connect", ws_add),
    route("websocket.disconnect", ws_disconnect),
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