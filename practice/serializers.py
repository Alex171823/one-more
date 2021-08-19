from rest_framework import serializers

from .models import Comments, Posts


class PostsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Posts
        fields = ['post_text', 'short_description', 'full_description', 'picture', 'is_draft', 'user']


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['text', 'username', 'post', 'is_published']

# """ TUTORIAL """
#
# from django.contrib.auth.models import User, Group
# from rest_framework import serializers
#
#
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']
#
#
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']
#
#
# """ TUTORIAL ENDS """
