from django.urls import path
from story.views import story_view

app_name = 'story'

urlpatterns = [
    path('', view=story_view, name='story')]
