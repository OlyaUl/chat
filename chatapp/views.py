from django.shortcuts import render
from channels import Group


# Create your views here.
def index(request):
    return render(request, 'chatapp/index.html', {})


'''def ws_connect(message):
    Group('chatroom').add(message.reply_channel)


def my_consumer(message):
    pass

# Connected to websocket.connect
def ws_add(message):
    # Accept the incoming connection
    message.reply_channel.send({"accept": True})
    # Add them to the chat group
    Group("chat").add(message.reply_channel)

# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)
'''
# Group('chatroom').send({"text"})
