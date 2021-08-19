from rest_framework import viewsets
from rest_framework.fields import CurrentUserDefault

from .models import Comments, Posts
from .serializers import CommentsSerializer, PostsSerializer


class PostsModelApi(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    user = CurrentUserDefault()


class CommentsModelApi(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
