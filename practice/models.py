from django.contrib.auth.models import User as User
from django.db import models


class Posts(models.Model):
    post_text = models.TextField()
    short_description = models.CharField(max_length=255)
    full_description = models.TextField()
    picture = models.CharField(max_length=255)
    is_draft = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f"{self.post_text} {self.short_description} {self.full_description} {self.picture} {self.is_draft} {self.user}"  # noqa W292


class Comments(models.Model):

    class LoanStatus(models.IntegerChoices):
        PUBLISHED = 1
        IS_DRAFT = 0

    text = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, default=1)

    is_published = models.BooleanField(default=0)

    def __str__(self):
        return f"{self.text} {self.username} {self.post}"

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
