import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100,default='untitled')
    author = models.CharField(max_length=100,default='unknown')
    body = models.TextField(blank=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def was_created_recently(self):
        now = timezone.now()
        return now-datetime.timedelta(days=1)<=self.create_date<=now

    def __str__(self):
        return '"%s" created by %s' % (self.title,self.author)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=20,default='unknown')
    author_id = models.IntegerField(default=0)
    body = models.TextField(blank=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment by %s' % self.author

class Profile(models.Model):
    M = 'Male'
    F = 'Female'
    U = 'Unknown'
    sex_choice = (
        (M, 'Male'),
        (F, 'Female'),
        (U, 'Unknown')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sex = models.CharField(max_length=1, choices=sex_choice)
    age = models.IntegerField(default=0)
    introduction = models.TextField(default='There is no introduction')
    have_edited = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
