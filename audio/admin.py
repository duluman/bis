from django.contrib import admin
from audio.models import AudioModel, AudioTitleTop, AudioModelSound
# Register your models here.


class AudioTabularLine(admin.TabularInline):
    model = AudioModelSound
    extra = 0


class AudioModelAdmin(admin.ModelAdmin):
    inlines = [AudioTabularLine]
    list_display = ['title', 'author']

    class Meta:
        model = AudioModel


admin.site.register(AudioModel, AudioModelAdmin)
admin.site.register(AudioTitleTop)
