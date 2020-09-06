from django.urls import path
from book.views import book_view, details, details_pdf

app_name = 'book'

urlpatterns = [
    path('', view=book_view, name='book'),
    path('details/<int:bookmodel_id>/', view=details, name='details'),
    path('pdf/<int:id>/', view=details_pdf, name='pdf_details'),
]
