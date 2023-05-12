from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


def upload_path_image(instance, filename):
    return 'book_images/{0}/{1}'.format(instance.author, filename)


# Create your models here.

class Book(models.Model):
    title = models.CharField()
    description = models.TextField()
    image = models.ImageField(upload_to=upload_path_image)
    release_date = models.DateField()
    price = models.IntegerField()
    author = models.CharField(max_length=30)
    reviews_quantity = models.IntegerField(default=0)
    # rating = models.FloatField()  #   get average from Review.objects.filter(author=user)?

    class Meta:
        verbose_name = "book"
        verbose_name_plural = "books"

    def __str__(self):
        return f"Book with title: {self.title} and ID: {self.id}"


class Review(models.Model):
    # unique?
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')  # null=True, blank=True?
    review = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # null=True, blank=True?
    rating = models.PositiveSmallIntegerField(null=True)

    class Meta:
        verbose_name = "review"
        verbose_name_plural = "reviews"

    def __str__(self):
        return f"Review from user: {self.author}, for {self.book}"
