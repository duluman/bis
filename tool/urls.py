from django.urls import path
from tool.views import tool_view, details

app_name = 'tool'

urlpatterns = [
    path('', view=tool_view, name='tool'),
    path('details/<int:toolmodel_id>/', view=details, name='details')]
