from django.shortcuts import render
from gratitude.models import GratitudeAndThankfulness, GratitudeBackground
from gratitude.models import EnGratitudeAndThankfulness, EnGratitudeBackground

# Create your views here.


def gratitude_view(request):
    gratitude_list = GratitudeAndThankfulness.objects.all()
    background_list = GratitudeBackground.objects.all()

    context = {
        'gratitude_list_template': gratitude_list,
        'background_list_template': background_list}

    return render(request, 'gratitude/gratitude_and_thankfulness.html', context)


def en_gratitude_view(request):
    gratitude_list = EnGratitudeAndThankfulness.objects.all()
    background_list = EnGratitudeBackground.objects.all()

    context = {
        'gratitude_list_template': gratitude_list,
        'background_list_template': background_list}

    return render(request, 'gratitude/en_gratitude_and_thankfulness.html', context)
