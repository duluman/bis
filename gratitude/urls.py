from django.urls import path
from gratitude.views import gratitude_view

app_name = 'gratitude'

urlpatterns = [
    path('', view=gratitude_view, name='gratitude')]
