"""admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from apscheduler.scheduler import Scheduler
import main
import xadmin


sched = Scheduler()
@sched.interval_schedule(seconds=6000)
def my_task():
    main.main()

sched.start()

urlpatterns = [
    #url(r'^xadmin/', include(xadmin.site.urls)),
    url(r'^', include('detail.urls', namespace='detail')),
    url(r'^user/', include('users.urls', namespace='users')),
    url(r'^record/', include('operations.urls', namespace='operations')),
    url(r'^reports/', include('reports.urls', namespace='reports')),
    url(r'^ansible/', include('taskdo.urls', namespace='taskdo')),
]


