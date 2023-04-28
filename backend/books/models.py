from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


def upload_path_image(instance, filename):
    return 'book_images/{0}/{1}'.format(instance.author, filename)


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_path_image)
    release_date = models.DateField()
    price = models.IntegerField()
    author = models.CharField(max_length=30)
    # rating = models.FloatField()

    class Meta:
        verbose_name = "book"

    def __str__(self):
        return f"Book with title: {self.title}"


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(null=True)

    # validate field 'rating' for admin https://django.fun/ru/docs/django/4.1/ref/validators/

    class Meta:
        verbose_name = "review"

    def __str__(self):
        return f"Review from user: {self.author}"
