from django.contrib import admin
from audio.models import AudioModel, AudioTitleTop, AudioModelSound
from audio.models import EnAudioModel, EnAudioTitleTop, EnAudioModelSound
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


# English


class EnAudioTabularLine(admin.TabularInline):
    model = EnAudioModelSound
    extra = 0


class EnAudioModelAdmin(admin.ModelAdmin):
    inlines = [EnAudioTabularLine]
    list_display = ['title', 'author']

    class Meta:
        model = EnAudioModel


admin.site.register(EnAudioModel, EnAudioModelAdmin)
admin.site.register(EnAudioTitleTop)
