from django.urls import path
from interview.views import interview_view

app_name = 'interview'

urlpatterns = [path('', view=interview_view, name='interview')]
