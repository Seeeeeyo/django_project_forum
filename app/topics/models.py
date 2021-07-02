from django.db import models
from user.models import User
from django.utils import timezone


class Topic(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField("date published", default=timezone.now())  # verbose used to debug
    text = models.TextField()
    solved = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def get_last_message_author(self):
        if self.response_set.all().last() is not None:
            return self.response_set.all().last().get_author()

    def get_last_message_date(self):
        if self.response_set.all().last() is not None:
            return self.response_set.all().last().get_date()

    def get_replies_count(self):
        return self.response_set.count()

    def __str__(self):
        return self.title


class Response(models.Model):
    date = models.DateTimeField("date published", default=timezone.now())  # verbose used to debug
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def get_author(self):
        return str(self.author)

    def get_date(self):
        return self.date

    def get_avatar(self):
        return self.author.get_avatar_url()

    def __str__(self):
        return self.text