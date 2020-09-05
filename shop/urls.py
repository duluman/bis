from django.urls import path
from shop.views import shop_view, order_view, books_view


app_name = 'shop'

urlpatterns = [
    path('', view=shop_view, name='shop'),
    path('order/', view=order_view, name='order'),
    path('order/books/', view=books_view, name='books'),
]

