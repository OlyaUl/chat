from django.shortcuts import render
from channels import Group
from django.views.generic import View, ListView, TemplateView

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.views.generic import CreateView
from .forms import UserForm


def index(request):
    return render(request, 'chatapp/index.html', {})


class ChatView(TemplateView):
    template_name = 'chatapp/send.html'


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/chatapp/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'chatapp/login.html', {})


class UserFormView(CreateView):
    form_class = UserForm
    template_name = 'chatapp/registration.html'
    success_url = '/chatapp/'

    def form_valid(self, form):
        response = super(UserFormView, self).form_valid(form)
        self.object.set_password(form.cleaned_data['password'])
        self.object.save()
        return response

    def get_context_data(self, **kwargs):
        return super(UserFormView, self).get_context_data(**kwargs)


'''@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/chatapp/')'''''

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
