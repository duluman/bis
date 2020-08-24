from django.contrib import admin
from direction.models import Direction, DirectionTitleTop
# Register your models here.


class DirectionAdmin(admin.ModelAdmin):

    list_display = ['title']

    class Meta:
        model = Direction


admin.site.register(Direction, DirectionAdmin)
admin.site.register(DirectionTitleTop)
