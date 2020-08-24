from django.db import models

# Create your models here.


class Direction(models.Model):
    title = models.CharField(max_length=255, default=None, blank=True)
    body = models.TextField(default=None, blank=True)
    picture = models.ImageField(upload_to='direction/', blank=True, null=True)

    def __str__(self):
        return self.title


class DirectionTitleTop(models.Model):
    title = models.CharField(max_length=255, default=None, blank=True)
    subtitle = models.CharField(max_length=255, default=None, blank=True)
    picture = models.ImageField(upload_to='direction/', blank=True, null=True)

    def __str__(self):
        return self.title
