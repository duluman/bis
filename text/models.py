from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class TextModel(models.Model):

    title = models.CharField(max_length=255, default=None, blank=True)
    subtitle = models.CharField(max_length=255, default=None, blank=True)
    picture = models.ImageField(upload_to='text/', blank=True, null=True)
    date_of_post = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class BodyTextModel(models.Model):
    heading = models.ForeignKey(TextModel, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=255, default=None, blank=True)
    body = models.TextField(default=None, blank=True)
    image = models.ImageField(upload_to='text/', blank=True, null=True)

    def __str__(self):
        return self.title


class TextPageBackground(models.Model):
    title = models.CharField(max_length=255, default=None, blank=True)
    subtitle = models.CharField(max_length=255, default=None, blank=True)
    picture = models.ImageField(upload_to='text/', blank=True, null=True)

    def __str__(self):
        return self.title

