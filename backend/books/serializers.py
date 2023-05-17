from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Book, Review
# from django.contrib.auth.models import User

User = get_user_model()


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class ReviewSerializer(serializers.ModelSerializer):
    review = serializers.CharField()
    author = AuthorSerializer()
    rating = serializers.IntegerField(max_value=10, min_value=1)

    class Meta:
        model = Review
        fields = ["review", "rating", "author"]
        # fields = "__all__"
        validators = [
            UniqueTogetherValidator(
                queryset=Review.objects.all(),
                fields=['author', 'book']
            )
        ]


class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    # description = serializers.CharField()
    image = serializers.ImageField(required=False)
    # release_date = serializers.DateField()
    # price = serializers.IntegerField()
    author = serializers.CharField(max_length=30)
    reviews_quantity = serializers.IntegerField(default=0, read_only=True)
    rating = serializers.FloatField(min_value=0.0, max_value=10.0, default=0.0, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    # quantity = serializers.IntegerField(read_only=True)

    class Meta:
        model = Book
        fields = ["id", "title", "description", "reviews", "image", "release_date", "price", "author", "reviews_quantity", "rating"]
        # exclude = ['quantity', ]
        # fields = "__all__"


# class FavouritesSerializer(serializers.Serializer):
#     book_id = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), required=False)
