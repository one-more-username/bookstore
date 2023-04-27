from django.db import models


# Create your models here.

class Basket(models.Model):
    class Meta:
        verbose_name = "basket"

    def __str__(self):
        return f"Book with id {self.book_id} added to the order"


class Order(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    book_id = models.IntegerField()

    class Meta:
        verbose_name = "order"

    def __str__(self):
        return f"Book with id {self.book_id} added to the order"
