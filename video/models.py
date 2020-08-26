from django.db import models

# Create your models here.


class VideoModel(models.Model):
    title = models.CharField(max_length=255, default=None, blank=True)
    category = models.CharField(max_length=255, default=None, blank=True)
    youtube_video_link = models.CharField(max_length=255, default=None)

    def __str__(self):
        return self.title


class VideoTitleTop(models.Model):
    title = models.CharField(max_length=255, default=None, blank=True)
    subtitle = models.CharField(max_length=255, default=None, blank=True)
    picture = models.ImageField(upload_to='video/', blank=True, null=True)

    def __str__(self):
        return self.title
