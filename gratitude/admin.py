from django.contrib import admin
from gratitude.models import GratitudeAndThankfulness, GratitudeBackground
# Register your models here.


class GratitudeAdmin(admin.ModelAdmin):

    list_display = ('title', 'youtube', 'date')

    class Meta:
        model = GratitudeAndThankfulness


admin.site.register(GratitudeAndThankfulness, GratitudeAdmin)
admin.site.register(GratitudeBackground)
