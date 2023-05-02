from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = "profile"

    def __str__(self):
        return f"Profile for user: {self.user}"


class Favourite(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    book_id = models.IntegerField()  # readonly
    quantity = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = "favourite"

    def __str__(self):
        return f"Book with id: {self.book_id}"
