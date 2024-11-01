"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.shortcuts import redirect
from django.urls import path, re_path

from BeMindfull.views import custom_login, custom_register, custom_home, custom_logout


def redirect_to_home(request):
    return redirect('home')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', custom_login, name='login'),
    path('register/', custom_register, name='register'),
    path('home/', custom_home, name='home'),
    path('logout/', custom_logout, name='logout'),
    re_path(r'^,*$', redirect_to_home, name='redirect_to_home')
]
