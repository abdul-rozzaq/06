from django.urls import path
from .views import books_page, customers_page, orders_page

urlpatterns = [
    path('', books_page, name='books_page'),
    path('customers/', customers_page, name='customers_page'),
    path('orders/', orders_page, name='orders_page'),
]
