from django.db import models

# Create your models here.


class AudioModel(models.Model):
    title = models.CharField(max_length=355, default=None, blank=True)  # name
    author = models.CharField(max_length=355, default=None, blank=True)  # singer
    category = models.CharField(max_length=255, default=None, blank=True)  # tags
    picture = models.ImageField(upload_to='audio/', blank=True, null=True)  # image
    
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
    SIZE_CHOICE = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    ]

    title_size = models.CharField(
        max_length=100,
        default="1",
        choices=SIZE_CHOICE,
        blank=True,
        null=True)

    COLOR_CHOICE = [
        ("white", "white"),
        ("black", "black"),
        ("cyan", "cyan"),
        ("indigo", "indigo"),
        ("blue", "blue"),
        ("red", "red"),
        ("green", "green"),
        ("amber", "amber"),
        ("pink", "pink")]

    title_color = models.CharField(
        max_length=100,
        choices=COLOR_CHOICE,
        default=None,
        blank=True,
        null=True
    )

    subtitle = models.CharField(max_length=455, default=None, blank=True)

    subtitle_size = models.CharField(
        max_length=100,
        default="5",
        choices=SIZE_CHOICE,
        blank=True,
        null=True)

    subtitle_color = models.CharField(
        max_length=100,
        choices=COLOR_CHOICE,
        default=None,
        blank=True,
        null=True
    )

    mask_overlay = models.CharField(max_length=255, default='rgba-white-light', blank=True, null=True)
    picture = models.ImageField(upload_to='audio/', blank=True, null=True)

    def __str__(self):
        return self.title
