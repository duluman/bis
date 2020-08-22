from django.db import models

# Create your models here.


class ProfessionalDevelopment(models.Model):
    title = models.CharField(max_length=255, default=None, blank=True)
    body = models.TextField(default=None, blank=True)
    date = models.CharField(max_length=255, default=None, blank=True)
    picture = models.ImageField(upload_to='professional/', blank=True, null=True)

    class Meta:
        ordering = ['-title']

    def __str__(self):
        return self.title


class ProfessionalBackground(models.Model):
    title = models.CharField(max_length=255, default=None, blank=True)
    subtitle = models.CharField(max_length=255, default=None, blank=True)
    picture = models.ImageField(upload_to='professional/', blank=True, null=True)

    def __str__(self):
        return self.title
