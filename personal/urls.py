from django.urls import path
from personal.views import personal_view, en_personal_view

app_name = 'personal'

urlpatterns = [
    path('', view=personal_view, name='personal'),
    path('en/', view=en_personal_view, name='en_personal'),
]
