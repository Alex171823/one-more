from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path('', views.startpage, name='startpage'),

    path('people/', views.PeopleListView.as_view(), name='list-people'),
    path('detailperson/<int:pk>', views.PeopleDetailView.as_view(), name='detail-person'),
    path('films/', cache_page(10)(views.films_list), name='list-films'),
    path('detailfilm/<int:pk>', views.FilmsDetailView.as_view(), name='detail-film'),
]
