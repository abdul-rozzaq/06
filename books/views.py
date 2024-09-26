from django.shortcuts import render
from .models import Book, Customer, Order


def books_page(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})


def customers_page(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})


def orders_page(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': orders})

