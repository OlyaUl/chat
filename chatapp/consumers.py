from channels.auth import channel_session_user, channel_session_user_from_http
from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group


# Connected to websocket.connect
def ws_add(message):
    # Accept the connection
    message.reply_channel.send({"accept": True})
    # Add to the chat group
    Group("chat").add(message.reply_channel)


# Connected to websocket.receive
@channel_session_user_from_http
def ws_message(message):
    print(message.user)
    Group("chat").send({
        "text": "[{}] {}".format(message.user.username, message.content['text']),
    })


# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)


def http_consumer(message):
    # Make standard HTTP response - access ASGI path attribute directly
    response = HttpResponse("Hello world! You asked for %s" % message.content['path'])
    # Encode that response into message format (ASGI)
    for chunk in AsgiHandler.encode_response(response):
        message.reply_channel.send(chunk)


# def ws_message(message):
#     # ASGI WebSocket packet-received and send-packet message types
#     # both have a "text" key for their textual data.
#     print(dir(message))
#     message.reply_channel.send({
#         "text": message.content['text'],
#     })
