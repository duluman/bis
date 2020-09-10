from django.urls import path
from audio.views import audio_view, audio_single_view
from audio.views import en_audio_view, en_audio_single_view

app_name = 'audio'

urlpatterns = [
    path('', view=audio_view, name='audio'),
    path('details/<int:audiomodel_id>/', view=audio_single_view, name='details'),
    path('en/', view=en_audio_view, name='en_audio'),
    path('en/details/<int:enaudiomodel_id>/', view=en_audio_single_view, name='en_details'),
]
