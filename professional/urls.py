from django.urls import path
from professional.views import professional_view, en_professional_view

app_name = 'professional'

urlpatterns = [
    path('', view=professional_view, name='professional'),
    path('en/', view=en_professional_view, name='en_professional')]
