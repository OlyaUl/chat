from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^ws_connect$', views.ws_connect, name='ws_connect'),

]