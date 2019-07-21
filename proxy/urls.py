# coding:utf-8

from django.conf.urls import include, url
from proxy import views

urlpatterns = [
    url(r'^count/$', views.proxy_num),
    url(r'^one$', views.proxy),
]
