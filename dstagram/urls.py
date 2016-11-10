"""dstagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

from photo import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),



    # template 디버깅용임 건들지마셈
    url(r'^debug/login', views.debug_login, name='login'),
    url(r'^debug/main', views.debug_main, name='main'),
    url(r'^debug/signup', views.debug_signup, name='signup'),
    url(r'^debug/insert', views.debug_insert, name='insert'),
    url(r'^debug/update-page', views.debug_update_page, name='update-page'),
    url(r'^debug/update', views.debug_update, name='update'),
]
