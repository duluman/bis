from django.urls import path
from professional.views import professional_view

app_name = 'professional'

urlpatterns = [
    path('', view=professional_view, name='professional')]
