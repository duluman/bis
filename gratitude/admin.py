from django.contrib import admin
from gratitude.models import GratitudeAndThankfulness, GratitudeBackground
from gratitude.models import EnGratitudeAndThankfulness, EnGratitudeBackground
# Register your models here.


class GratitudeAdmin(admin.ModelAdmin):

    list_display = ('title', 'youtube', 'date')

    class Meta:
        model = GratitudeAndThankfulness


admin.site.register(GratitudeAndThankfulness, GratitudeAdmin)
admin.site.register(GratitudeBackground)


class EnGratitudeAdmin(admin.ModelAdmin):

    list_display = ('title', 'youtube', 'date')

    class Meta:
        model = EnGratitudeAndThankfulness


admin.site.register(EnGratitudeAndThankfulness, EnGratitudeAdmin)
admin.site.register(EnGratitudeBackground)
