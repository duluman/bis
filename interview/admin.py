from django.contrib import admin
from interview.models import InterviewModel, InterviewTitleTopBackground
# Register your models here.


@admin.register(InterviewModel)
class InterviewAdmin(admin.ModelAdmin):

    list_display = ['title']
    search_fields = ['title']

    class Meta:
        model = InterviewModel


admin.site.register(InterviewTitleTopBackground)