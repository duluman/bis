from django.db import models
from django.utils import timezone
# Create your models here.


class EventModel(models.Model):
    title = models.CharField(max_length=255, default=None, blank=True)
    body = models.TextField(default=None, blank=True)
    picture = models.ImageField(upload_to='event/', blank=True, null=True)
    youtube = models.CharField(max_length=255, default=None, blank=True)
    date_of_post = models.DateTimeField(default=timezone.now)
    link_title = models.CharField(max_length=255, default=None, blank=True)
    link = models.CharField(max_length=255, default=None, blank=True)

    class Meta:
        ordering = ['-date_of_post']

    def __str__(self):
        return self.title


class EventBackground(models.Model):
    title = models.CharField(max_length=255, default=None, blank=True)
    subtitle = models.CharField(max_length=255, default=None, blank=True)
    picture = models.ImageField(upload_to='event/', blank=True, null=True)

    def __str__(self):
        return self.title
