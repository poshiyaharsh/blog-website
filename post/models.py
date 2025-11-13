from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

def now_str():
    return datetime.now().strftime("%d %B %Y")

class Post(models.Model):
    postname = models.CharField(max_length=600)
    category = models.CharField(max_length=600)
    image = models.ImageField(upload_to='images/posts', blank=True, null=True)
    content = models.TextField()
    time = models.CharField(default=now_str, max_length=100, blank=True)
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.postname)

class Comment(models.Model):
    content = models.CharField(max_length=200)
    time = models.CharField(default=now_str, max_length=100, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}.{self.content[:20]}..."
