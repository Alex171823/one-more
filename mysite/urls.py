from django.urls import path

from mysite import views

urlpatterns = [
    path('', views.start),
    path('author/', views.authors),
    path('author/<int:pk>', views.author_detail, name='author_detail_url'),
    path('publisher/', views.publisher),
    path('publisher/<int:pk>', views.publisher_detail, name='publisher_detail_url'),
    path('store/', views.store),
    path('store/<int:pk>', views.store_detail, name='store_detail_url'),
    path('book/', views.books),
    path('book/<int:pk>', views.book_detail, name='book_detail_url'),
]
