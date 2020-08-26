from django.urls import path
from video.views import video_view

app_name = 'video'

urlpatterns = [path('', view=video_view, name='video')]
