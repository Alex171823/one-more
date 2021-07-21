from django.urls import path

from . import views


urlpatterns = [
    path('', views.startpage, name='startpage'),

    path('register/', views.register, name='register'),
]
