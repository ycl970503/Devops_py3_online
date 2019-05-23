# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^base/$', views.base),
    url(r'^report/$', views.report),
    url(r'^histogram/$', views.histogram),
    url(r'^rack', views.rack),
    url(r'^cab_add', views.cab_add),
    url(r'^phy_add', views.phy_add),

]
