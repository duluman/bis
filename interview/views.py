from django.shortcuts import render
from interview.models import InterviewModel, InterviewTitleTopBackground

# Create your views here.


def interview_view(request):
    interview_list = InterviewModel.objects.all()
    background_list = InterviewTitleTopBackground.objects.all()

    context = {
        'interview_list_template': interview_list,
        'background_list_template': background_list}

    return render(request, 'interview/interview.html', context)
