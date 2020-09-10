from django.contrib import admin
from personal.models import PersonalDevelopment, PersonalBackground, EnPersonalBackground, EnPersonalDevelopment
# Register your models here.


class MyStoryAdmin(admin.ModelAdmin):

    list_display = ('title', 'youtube', 'date')

    class Meta:
        model = PersonalDevelopment


admin.site.register(PersonalDevelopment, MyStoryAdmin)
admin.site.register(PersonalBackground)


class EnMyStoryAdmin(admin.ModelAdmin):

    list_display = ('title', 'youtube', 'date')

    class Meta:
        model = EnPersonalDevelopment


admin.site.register(EnPersonalDevelopment, EnMyStoryAdmin)
admin.site.register(EnPersonalBackground)
