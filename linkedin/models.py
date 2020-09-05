from django.db import models

# Create your models here.


class Education(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date = models.CharField(max_length=100)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title


class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date = models.CharField(max_length=100)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title
