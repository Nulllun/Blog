import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Post, Comment


class PostModelTests(TestCase):

    def test_was_created_recently(self):
        time = timezone.now() - datetime.timedelta(hours=23,seconds=59)
        recent_post = Post(create_date=time,body='Testing')
        self.assertIs(recent_post.was_created_recently(), True)