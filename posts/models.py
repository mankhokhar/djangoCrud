from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(blank=True)
    pub_date = models.DateTimeField(default=timezone.now())
    reacts = models.IntegerField(default=0)
    image = models.ImageField(blank=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.TextField(blank=True)
