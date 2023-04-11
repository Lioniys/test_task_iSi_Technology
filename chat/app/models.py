from django.db import models
from django.conf import settings


class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=5000)
    thread = models.ForeignKey("Thread", on_delete=models.CASCADE, related_name="message")
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']


class Thread(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']


class ThreadUser(models.Model):
    thread = models.ForeignKey("Thread", on_delete=models.CASCADE, related_name="participants")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
