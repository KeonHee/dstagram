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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as login_views

from photo import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(
        r'^accounts/login/',
        login_views.login,
        name='login',
        kwargs={
            'template_name': 'login.html',
        }
    ),
    url(
        r'^accounts/logout/',
        login_views.logout,
        name='logout'
    ),
    url(r'^photos/', views.photo_list, name='photos'),
    url(r'^photos/(?P<photo_id>\d+)/$', views.photo_detail, name='photo_detail'),

    # template 디버깅용임 건들지마셈
    #url(r'^debug/login', views.debug_login, name='login'),
    url(r'^debug/main', views.debug_main, name='main'),
    url(r'^debug/signup', views.debug_signup, name='signup'),
    url(r'^debug/insert', views.debug_insert, name='insert'),
    url(r'^debug/update-page', views.debug_update_page, name='update-page'),
    url(r'^debug/update', views.debug_update, name='update'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
