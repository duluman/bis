from django.db import models

# Create your models here.


class AudioModel(models.Model):
    title = models.CharField(max_length=355, default=None, blank=True)  # name
    author = models.CharField(max_length=355, default=None, blank=True)  # singer
    category = models.CharField(max_length=255, default=None, blank=True)  # tags
    picture = models.ImageField(upload_to='audio/', blank=True, null=True)  # image
    audio_file = models.FileField(upload_to='audio/')  # song
    body = models.TextField(default=None, blank=True)

    def __str__(self):
        return self.title


class AudioModelSound(models.Model):
    connection = models.ForeignKey(AudioModel, on_delete=models.CASCADE, default=None)
    audio_name = models.CharField(max_length=355, default=None, blank=True)
    audio = models.FileField(upload_to='audio/')
    body = models.TextField(default=None, blank=True)

    def __str__(self):
        return self.audio_name


class AudioTitleTop(models.Model):
    title = models.CharField(max_length=255, default=None, blank=True)
    subtitle = models.CharField(max_length=255, default=None, blank=True)
    picture = models.ImageField(upload_to='audio/', blank=True, null=True)

    def __str__(self):
        return self.title
