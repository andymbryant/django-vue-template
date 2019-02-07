from django.db import models

class Post(models.Model):
    userId = models.IntegerField()
    title = models.CharField(max_length = 100)
    body = models.CharField(max_length = 500)

class Comment(models.Model):
    postId = models.IntegerField()
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    body = models.CharField(max_length = 500)