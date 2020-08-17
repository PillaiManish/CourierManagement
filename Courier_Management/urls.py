"""Courier_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from homepage.views import f_homepage,f_track,f_add,f_update
from accounts.views import f_login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', f_homepage),
    url(r'^track/', f_track),
    url(r'^login/', f_login),
    url(r'^add/', f_add),
    url(r'^update/', f_update),

    

]
