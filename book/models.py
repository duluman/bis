from django.db import models
from django.utils import timezone

# Create your models here.


class BookModel(models.Model):

    title = models.CharField(max_length=255, default=None, blank=True)
    subtitle = models.CharField(max_length=255, default=None, blank=True)
    picture = models.ImageField(upload_to='book/', blank=True, null=True)
    date_of_post = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class BodyTextModel(models.Model):
    heading = models.ForeignKey(BookModel, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=255, default=None, blank=True)
    body = models.TextField(default=None, blank=True)

    def __str__(self):
        return self.title

