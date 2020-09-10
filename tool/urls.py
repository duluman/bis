from django.urls import path
from tool.views import tool_view, details
from tool.views import en_tool_view, en_details

app_name = 'tool'

urlpatterns = [
    path('', view=tool_view, name='tool'),
    path('details/<int:toolmodel_id>/', view=details, name='details'),
    path('en/', view=en_tool_view, name='en_tool'),
    path('en/details/<int:entoolmodel_id>/', view=en_details, name='en_details')
    ]

