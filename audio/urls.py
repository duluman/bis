from django.urls import path
from audio.views import audio_view, audio_single_view

app_name = 'audio'

urlpatterns = [
    path('', view=audio_view, name='audio'),
    path('details/<int:audiomodel_id>/', view=audio_single_view, name='details')]
