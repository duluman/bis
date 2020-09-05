from django.db import models

# Create your models here.


class TypeModel(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class BookModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    type = models.ForeignKey(TypeModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
