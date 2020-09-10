from django.shortcuts import render
from event.models import EventModel, EventBackground
from event.models import EnEventModel, EnEventBackground

# Create your views here.


def event_view(request):
    event_list = EventModel.objects.all()
    background_list = EventBackground.objects.all()

    context = {
        'event_list_template': event_list,
        'background_list_template': background_list}

    return render(request, 'event/events.html', context)


def en_event_view(request):
    event_list = EnEventModel.objects.all()
    background_list = EnEventBackground.objects.all()

    context = {
        'event_list_template': event_list,
        'background_list_template': background_list}

    return render(request, 'event/en_events.html', context)

