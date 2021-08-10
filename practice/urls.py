from django.urls import path

from . import views


urlpatterns = [
    path('', views.startpage, name='startpage'),

    path('register/', views.register, name='register'),
    path('posts_create/', views.PostsCreateView.as_view(), name = 'posts_create'),
    path('posts_update/<int:pk>', views.PostsUpdateView.as_view(), name = 'posts_update'),
    path('posts_list/', views.PostsListView.as_view(), name='posts_list'),
    path('posts_detail/<int:pk>', views.PostsDetailView.as_view(), name='posts_detail'),

    path('comments_create/', views.CommentsCreateView.as_view(), name='comments_create'),
]
