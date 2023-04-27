from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


def upload_path_autor(instance, filename):
    return 'profile_images/{0}/{1}'.format(instance.user, filename)


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_path_autor)  # blank=True, null=True
    release_date = models.DateField()
    price = models.IntegerField()
    author = models.CharField()
    feedback_quantity = models.CharField()
    rating = models.FloatField()
    buyer = models.ForeignKey(User, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "book"
        # verbose_name_plural = "profile"

    def __str__(self):
        return f"Book with title: {self.title}"
