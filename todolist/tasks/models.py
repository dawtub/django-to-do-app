from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    completed = models.BooleanField(max_length=10, default=False)
    time = models.DateTimeField("time published", auto_now_add=True)

    def __str__(self):
        return self.text

    def is_done(self):
        return self.completed
