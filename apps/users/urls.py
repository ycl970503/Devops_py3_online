# -*-coding:utf-8-*-
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^base$', views.base),
    url(r'^login/$', views.login),
    url(r'^register', views.register),
    url(r'^login_haddle/$', views.login_haddle),
    url(r'^logout/$', views.logout),
    url(r'^user_center/$', views.user_center),
]

