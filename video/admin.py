from django.contrib import admin
from video.models import VideoModel, VideoTitleTop
# Register your models here.


@admin.register(VideoModel)
class VideoAdmin(admin.ModelAdmin):

    list_display = ['title']
    search_fields = ['title']

    class Meta:
        model = VideoModel


admin.site.register(VideoTitleTop)
