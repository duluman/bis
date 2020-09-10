from django.contrib import admin
from interview.models import InterviewModel, InterviewTitleTopBackground
from interview.models import EnInterviewModel, EnInterviewTitleTopBackground
# Register your models here.


@admin.register(InterviewModel)
class InterviewAdmin(admin.ModelAdmin):

    list_display = ['title']
    search_fields = ['title']

    class Meta:
        model = InterviewModel


admin.site.register(InterviewTitleTopBackground)


@admin.register(EnInterviewModel)
class EnInterviewAdmin(admin.ModelAdmin):

    list_display = ['title']
    search_fields = ['title']

    class Meta:
        model = EnInterviewModel


admin.site.register(EnInterviewTitleTopBackground)
