from django.contrib.auth import get_user_model
from django.db import models

from books.models import Book

User = get_user_model()


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    favourites = models.ManyToManyField(Book, blank=True, default=None)
    purchase_history = models.ManyToManyField(Book, blank=True, default=None, related_name='purchase_history')

    class Meta:
        verbose_name = "profile"

    def __str__(self):
        return f"Profile for user: {self.user}"
