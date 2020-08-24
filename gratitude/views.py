from django.shortcuts import render
from gratitude.models import GratitudeAndThankfulness, GratitudeBackground

# Create your views here.


def gratitude_view(request):
    gratitude_list = GratitudeAndThankfulness.objects.all()
    background_list = GratitudeBackground.objects.all()

    context = {
        'gratitude_list_template': gratitude_list,
        'background_list_template': background_list}

    return render(request, 'gratitude/gratitude_and_thankfulness.html', context)

