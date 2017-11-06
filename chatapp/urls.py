from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^ws_connect$', views.ws_connect, name='ws_connect'),
    url(r'^chat_view/$', views.ChatView.as_view(), name='chat_view'),
    url(r'^login_view/$', views.login_view, name='login_view'),
    url(r'^register_view/$', views.UserFormView.as_view(), name='register_view'),
    # url(r'^logout/$', views.user_logout, name='logout'),
]
