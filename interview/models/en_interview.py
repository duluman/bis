from django.db import models

# Create your models here.


class EnInterviewModel(models.Model):
    title = models.CharField(max_length=255, default=None, blank=True)
    category = models.CharField(max_length=255, default=None, blank=True)
    youtube_video_link = models.CharField(max_length=255, default=None)

    def __str__(self):
        return self.title


class EnInterviewTitleTopBackground(models.Model):
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
    picture = models.ImageField(upload_to='interview/', blank=True, null=True)

    def __str__(self):
        return self.title
