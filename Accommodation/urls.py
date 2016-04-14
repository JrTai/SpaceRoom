"""Accommodation URL Configuration

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
admin.autodiscover()
from landlords.views import room, list_landlords, message
from views import meta, welcome, set_c, get_c, index#, login, logout
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^room/$', room),
    #url(r'^room/(\d{1,5})/$', room), # one more argument (\d{1,5}) as input to room
    url(r'^meta/$', meta),
    url(r'^welcome/$', welcome),
    url(r'^landlords_list/$', list_landlords),
    url(r'^message/(\d{1,5})/$', message),
    url(r'^set_c/$', set_c),
    url(r'^get_c/$', get_c),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout, {'template_name': 'logout.html'}),
    url(r'^index/$', index),
]
