from django.db import models


class RoGdprModel(models.Model):

    title = models.CharField(max_length=255, default=None, blank=True)
    subtitle = models.CharField(max_length=255, default=None, blank=True)

    def __str__(self):
        return self.title


class RoGdprBodyTextModel(models.Model):
    heading = models.ForeignKey(RoGdprModel, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=255, default=None, blank=True)
    body = models.TextField(default=None, blank=True)

    def __str__(self):
        return self.title
