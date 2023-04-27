from django.contrib.auth import get_user_model
from django.db import models

from backend.books.models import Book

User = get_user_model()


# Create your models here.


class Profile(models.Model):
    favourites_list = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "book"

    def __str__(self):
        return f"Book with id {self.favourite_books} added to the favourites list"
