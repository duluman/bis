from django.urls import path
from event.views import event_view

app_name = 'event'

urlpatterns = [
    path('', view=event_view, name='event')]
