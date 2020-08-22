from django.contrib import admin
from personal.models import PersonalDevelopment, PersonalBackground
# Register your models here.


class MyStoryAdmin(admin.ModelAdmin):

    list_display = ('title', 'youtube', 'date')

    class Meta:
        model = PersonalDevelopment


admin.site.register(PersonalDevelopment, MyStoryAdmin)
admin.site.register(PersonalBackground)
