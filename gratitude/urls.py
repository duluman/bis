from django.urls import path
from gratitude.views import gratitude_view, en_gratitude_view

app_name = 'gratitude'

urlpatterns = [
    path('', view=gratitude_view, name='gratitude'),
    path('en/', view=en_gratitude_view, name='en_gratitude')]
