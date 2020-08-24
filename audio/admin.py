from django.contrib import admin
from audio.models import AudioModel, AudioTitleTop
# Register your models here.


class AudioModelAdmin(admin.ModelAdmin):

    list_display = ['title', 'author']

    class Meta:
        model = AudioModel


admin.site.register(AudioModel, AudioModelAdmin)
admin.site.register(AudioTitleTop)
