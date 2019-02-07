from .models import Post, Comment
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('userId', 'title', 'body')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('postId', 'name', 'email', 'body')