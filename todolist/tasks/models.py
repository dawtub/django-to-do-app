from django.db import models
from django.contrib.auth import get_user_model


class Task(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    completed = models.BooleanField(max_length=10, default=False)
    time = models.DateTimeField("time published", auto_now_add=True)

    def __str__(self):
        return self.text

    def is_done(self):
        return self.completed
