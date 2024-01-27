from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.SET_NULL, null=True)
    comment_text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def get_author_name(self):
        return self.author.get_full_name() or self.author.username

    def __str__(self):
        return self.comment_text if len(self.comment_text) <= 22 else f'{self.comment_text[:22]}...'
