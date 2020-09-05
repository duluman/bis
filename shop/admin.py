from django.contrib import admin
from shop.models import BookModel, TypeModel
# Register your models here.

admin.site.register(BookModel)
admin.site.register(TypeModel)