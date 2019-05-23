# -*- coding:utf-8 -*-
from django.conf.urls import url
from operations import views


urlpatterns = [
    url(r'^state_handdle/$', views.state_handdle),
    url(r'^module_deploy/$', views.module_deploy),
    url(r'module_operate/$',views.module_operate),
    url(r'^revise_net/(.+)/$',views.revise_net),
    url(r'^revisee_net/$',views.revisee_net),
    url(r'^login/(.+)/$',views.login)
]
