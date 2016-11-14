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

from photo import views as photo_views
urlpatterns = [

    url(
        r'^$',
        login_views.login,
        name='login',
        kwargs={
            'template_name': 'login.html',
        }
    ),
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
        name='logout',
    ),
    url(r'^photos/$', photo_views.photo_list, name='photos'),
    url(r'^photos/(?P<photo_id>\d+)$', photo_views.photo_detail, name='photo_detail'),


    url(r'^signup', photo_views.signup, name='signup'),
    url(r'^admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
