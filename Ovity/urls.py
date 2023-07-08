"""Ovity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('securelogin/', admin.site.urls),
    path('',views.home,name='home'),
    # Tech Events, Non Tech Events and Workshops
    path('waves/',include('waves_events.urls'),name='waves'),
    path('register/',include('register.urls'),name='register'),
    path('team/',include('team.urls'),name='team'),
    path('sponsers',views.sponsers,name='sponsers'),
    path('alumni', views.alumni, name='alumni'),
    path('miscellaneous', views.miscellaneous, name = 'misc'),
    path('accounts/',include('accounts.urls')),
    #Orders for my site
    path('my_orders/',include('my_orders.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)