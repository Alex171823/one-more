from django.urls import include, path

from rest_framework import routers

from . import views
from .api import CommentsModelApi, PostsModelApi

router = routers.DefaultRouter()
router.register(r'comments', CommentsModelApi)
router.register(r'posts', PostsModelApi)

urlpatterns = [
    path('api/', include(router.urls)),

    path('', views.startpage, name='startpage'),

    path('userprofile/<int:pk>', views.UserProfileView.as_view(), name='userprofile'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('change_password/<int:pk>', views.user_change_password, name='change_password'),

    path('posts_create/', views.PostsCreateView.as_view(), name='posts_create'),
    path('posts_update/<int:pk>', views.PostsUpdateView.as_view(), name='posts_update'),
    path('posts_list/', views.PostsListView.as_view(), name='posts_list'),
    path('posts_detail/<int:pk>', views.PostsDetailView.as_view(), name='posts_detail'),

    path('comments_create/', views.CommentsCreateView.as_view(), name='comments_create'),
]


# """ TUTORIAL """
#
# from django.urls import include, path
# from rest_framework import routers
#
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
#
# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns += [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]
#
# """ TUTORIAL ENDS """
