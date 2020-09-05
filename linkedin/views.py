from django.shortcuts import render
from linkedin.models import Education, Job
# Create your views here.


def cv_view(request):
    edu = Education.objects.all()
    jobs = Job.objects.all()

    context = {
        'education': edu,
        'jobs': jobs
    }

    template = 'linkedin/cv.html'

    return render(request, template, context)
