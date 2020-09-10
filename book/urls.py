from django.urls import path
from book.views import book_view, details, details_pdf
from book.views import en_book_view, en_details, en_details_pdf

app_name = 'book'

urlpatterns = [
    path('', view=book_view, name='book'),
    path('details/<int:bookmodel_id>/', view=details, name='details'),
    path('pdf/<int:id>/', view=details_pdf, name='pdf_details'),
    path('en/', view=en_book_view, name='en_book'),
    path('en/details/<int:enbookmodel_id>/', view=en_details, name='en_details'),
    path('en/pdf/<int:id>/', view=en_details_pdf, name='en_pdf_details'),
]
