from django.db import models


class Book(models.Model):
    image = models.ImageField(upload_to="book-images/")

    name = models.CharField(max_length=256)
    author = models.CharField(max_length=256)

    price = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name} - {self.author}"


class Customer(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)

    email = models.EmailField()
    phone = models.CharField(max_length=256)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    count = models.IntegerField()

    def total_price(self):
        return self.count * self.book.price
