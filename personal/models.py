from django.db import models
from django.utils import timezone
# Create your models here.


class PersonalDevelopment(models.Model):
    title = models.CharField(max_length=255, default=None, blank=True)
    body = models.TextField(default=None, blank=True)
    picture = models.ImageField(upload_to='personal/', blank=True, null=True)
    youtube = models.CharField(max_length=255, default=None, blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class PersonalBackground(models.Model):
    title = models.CharField(max_length=255, default=None, blank=True)
    subtitle = models.CharField(max_length=255, default=None, blank=True)
    picture = models.ImageField(upload_to='personal/', blank=True, null=True)

    def __str__(self):
        return self.title


