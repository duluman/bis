from django.urls import path
from interview.views import interview_view, en_interview_view

app_name = 'interview'

urlpatterns = [
    path('', view=interview_view, name='interview'),
    path('en/', view=en_interview_view, name='en_interview'),
]
