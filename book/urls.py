from django.urls import path
from book.views import book_view, details

app_name = 'book'

urlpatterns = [
    path('', view=book_view, name='book'),
    path('details/<int:bookmodel_id>/', view=details, name='details')]
