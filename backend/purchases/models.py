from django.contrib.auth import get_user_model
from django.db import models
from books.models import Book

User = get_user_model()


# Create your models here.

class ShoppingCart(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    # books = models.ManyToManyField("books.Book")
    books = models.ManyToManyField(Book)

    class Meta:
        verbose_name = "shopping cart"

    def __str__(self):
        return f"Shopping cart for user: {self.owner}"
