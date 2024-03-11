import uuid
from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_description = models.TextField()
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    created_by = models.CharField(max_length=36, default=uuid.uuid4)

    def __str__(self):
        return self.event_name