from django.contrib.auth import get_user_model
from django.db import models
from books.models import Book
from users.models import Profile

User = get_user_model()


# Create your models here.

class ShoppingCart(models.Model):
    owner = models.OneToOneField(Profile, on_delete=models.CASCADE)
    books_to_purchase = models.ManyToManyField(Book, default=None)

    class Meta:
        verbose_name = "shopping cart"

    def __str__(self):
        return f"Shopping cart for user: {self.owner}"
