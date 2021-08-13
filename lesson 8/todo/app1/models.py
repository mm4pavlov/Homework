from django.db import models


class Task(models.Model):
    text = models.CharField(max_length=300)
    is_completed = models.BooleanField(default=False)
