from django.db import models
from user.models import User

class Topic(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField("date published") #verbose used to debug
    text = models.TextField()
    solved = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Response(models.Model):
    date = models.DateTimeField("date published")  # verbose used to debug
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.text