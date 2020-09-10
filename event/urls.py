from django.urls import path
from event.views import event_view, en_event_view

app_name = 'event'

urlpatterns = [
    path('', view=event_view, name='event'),
    path('en/', view=en_event_view, name='en_event'),
]
