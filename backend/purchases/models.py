from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.

class ShoppingCart(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "shopping cart"

    def __str__(self):
        return f"Shopping cart for user: {self.owner}"


class BookForBuy(models.Model):
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    book_id = models.IntegerField()
    quantity = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = "book for buy"
        verbose_name_plural = "books for buy"

    def __str__(self):
        return f"Book with id: {self.book_id} in: {self.shopping_cart}"
