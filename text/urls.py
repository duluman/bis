from django.urls import path
from text.views import text_view, details, details_pdf_text
from text.views import en_text_view, en_details, en_details_pdf_text

app_name = 'text'

urlpatterns = [
    path('', view=text_view, name='text'),
    path('details/<int:textmodel_id>/', view=details, name='details'),
    path('pdf/<int:id>/', view=details_pdf_text, name='details_pdf_text'),
    path('en/', view=en_text_view, name='en_text'),
    path('en/details/<int:entextmodel_id>/', view=en_details, name='en_details'),
    path('en/pdf/<int:id>/', view=en_details_pdf_text, name='en_details_pdf_text'),
]
