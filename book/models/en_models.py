from django.db import models
from django.utils import timezone

# Create your models here.


class EnBookModel(models.Model):

    title = models.CharField(max_length=255, default=None, blank=True)
    subtitle = models.CharField(max_length=255, default=None, blank=True)
    picture = models.ImageField(upload_to='book/', blank=True, null=True)
    date_of_post = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class EnBodyTextModel(models.Model):
    heading = models.ForeignKey(EnBookModel, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=255, default=None, blank=True)
    body = models.TextField(default=None, blank=True)

    def __str__(self):
        return self.title


class EnTitleBookBackground(models.Model):
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
    picture = models.ImageField(upload_to='personal/', blank=True, null=True)

    def __str__(self):
        return self.title


class EnPdfUploadModel(models.Model):

    title = models.CharField(max_length=255, default=None, blank=True)
    author = models.CharField(max_length=255, default=None, blank=True)
    picture = models.ImageField(upload_to='pdf_book/', blank=True, null=True)
    pdf_url = models.CharField(max_length=255, default=None, blank=True)
    date_of_post = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
