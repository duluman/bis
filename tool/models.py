from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class ToolModel(models.Model):
    title = models.CharField(max_length=255, default=None, blank=True)
    subtitle = models.CharField(max_length=255, default=None, blank=True)
    picture = models.ImageField(upload_to='tool/', blank=True, null=True)
    date_of_post = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class BodyTextModel(models.Model):
    heading = models.ForeignKey(ToolModel, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=255, default=None, blank=True)
    body = models.TextField(default=None, blank=True)
    image = models.ImageField(upload_to='tool/', blank=True, null=True)

    def __str__(self):
        return self.title


class ToolPageBackground(models.Model):
    title = models.CharField(max_length=255, default=None, blank=True)
    subtitle = models.CharField(max_length=255, default=None, blank=True)
    picture = models.ImageField(upload_to='tool/', blank=True, null=True)

    def __str__(self):
        return self.title

