"""codeEditor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, path, include
from editcode.views import *


urlpatterns = [
    re_path('^$', home_page, name='home-page'),
    re_path('^\?message=.*$', home_page, name='home-page'),
    re_path('^view/$', view_file, name='home-page'),
    re_path('^delete/$', delete_file, name='home-page'),
    re_path('^save_file$', save_file, name='home-page'),
    re_path('^view/\?.*$', view_file, name='home-page'),
    re_path('^delete/\?.*$', delete_file, name='home-page'),
    re_path('^sign_in$', sign_in, name='sign-in'),
    re_path('^sign_up$', sign_up, name='sign-up'),
    re_path('^new_file$', new_file, name='sign-up'),
    path('admin/', admin.site.urls),
]
