from django.urls import path
from text.views import text_view, details, details_pdf_text

app_name = 'text'

urlpatterns = [
    path('', view=text_view, name='text'),
    path('details/<int:textmodel_id>/', view=details, name='details'),
    path('pdf/<int:id>/', view=details_pdf_text, name='details_pdf_text')]
