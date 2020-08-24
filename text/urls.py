from django.urls import path
from text.views import text_view, details

app_name = 'text'

urlpatterns = [
    path('', view=text_view, name='text'),
    path('details/<int:textmodel_id>/', view=details, name='details')]
