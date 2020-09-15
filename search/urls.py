from django.urls import path
from search.views import search_view, en_search_view

app_name = 'search'

urlpatterns = [
    path('', view=search_view, name='search'),
    path('en/', view=en_search_view, name='en_search'),
]
