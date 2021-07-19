from . import views
from django.urls import path


urlpatterns = [
    path('', views.startpage, name='startpage'),

    path('register/', views.register, name='register'),
]