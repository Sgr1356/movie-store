"""project9_onine_movie_stores URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from app9 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showmovies),
    path('oms/',views.oms,name="oms"),
     path('tollywood/',views.tollywood,name="tollywood"),
    path('bollywood/',views.bollywood,name="bollywood"),
    path('hollywood/',views.hollywood,name="hollywood"),
    path('playtollywood/',views.playtollywood,name="playtollywood"),
    path('playbollywood/',views.playbollywood,name="playbollywood"),
    path('playhollywood/',views.playhollywood,name="playhollywood"),
    path('booking/',views.booking,name="booking")
    # path('trailer/',views.playyoutubevideos,name="playyoutubevideos")
]
