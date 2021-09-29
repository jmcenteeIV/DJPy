from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('musicbox', views.musicview, name='musicbox'),
]