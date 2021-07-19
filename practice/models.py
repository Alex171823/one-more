from django.db import models
from django.contrib.auth.models import User as User


class Posts(models.Model):
    post_text = models.TextField()
    short_description = models.CharField(max_length=255)
    full_description = models.TextField()
    picture = models.CharField(max_length=255)
    is_draft = models.BooleanField()
    is_published = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post_text} {self.short_description} {self.full_description} {self.picture} {self.is_draft} {self.user}"


class Comments(models.Model):
	text = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	post = models.ForeignKey(Posts, on_delete=models.CASCADE, default=1)
