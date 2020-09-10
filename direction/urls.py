from django.urls import path
from direction.views import direction_view, en_direction_view

app_name = 'direction'

urlpatterns = [
    path('', view=direction_view, name='direction'),
    path('en/', view=en_direction_view, name='en_direction'),
]
