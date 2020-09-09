from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
# Create your models here.


class AppReview(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    comment = models.TextField(default=None)
    profession = models.CharField(max_length=255, blank=True, null=True)
    youtube_title = models.CharField(max_length=255, blank=True, null=True, default='Click pentru video')
    en_youtube_title = models.CharField(max_length=255, blank=True, null=True, default='Click here for the video')
    youtube_link = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("review:app_review")
