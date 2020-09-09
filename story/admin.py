from django.contrib import admin
from story.models import MyStory, StoryBackground, EnMyStory, EnStoryBackground
# Register your models here.


class MyStoryAdmin(admin.ModelAdmin):

    list_display = ('title', 'youtube', 'date')

    class Meta:
        model = MyStory


admin.site.register(MyStory, MyStoryAdmin)
admin.site.register(StoryBackground)


class EnMyStoryAdmin(admin.ModelAdmin):

    list_display = ('title', 'youtube', 'date')

    class Meta:
        model = EnMyStory


admin.site.register(EnMyStory, EnMyStoryAdmin)
admin.site.register(EnStoryBackground)
