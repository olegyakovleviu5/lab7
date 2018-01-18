"""untitled8 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from app.views import *
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main),
    url(r'^registration$', registration_form, name='registration'),
    url(r'^registration_1$', registration_1, name='registration_1'),
    url(r'^login1$', log_in, name='login1'),
    url(r'^login2$', log_in1, name='login2'),
    url(r'^logout$', logout_view, name='logout'),
    url(r'^logged_in$', logged_in_view, name='logged_in'),
    url(r'^logged_in_1$', logged_in, name='logged_in_1'),
    url(r'^registered$', user_registered, name='registered'),
]


