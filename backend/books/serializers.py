from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Book, Review


class ReviewSerializer(serializers.ModelSerializer):
    book = serializers.ReadOnlyField()
    review = serializers.CharField()
    author = serializers.ReadOnlyField(default=serializers.CurrentUserDefault())
    rating = serializers.IntegerField(max_value=10, min_value=1)

    class Meta:
        model = Review
        fields = "__all__"
        validators = [
            UniqueTogetherValidator(
                queryset=Review.objects.all(),
                fields=['author', 'book']
            )
        ]


class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    description = serializers.CharField()
    image = serializers.ImageField(required=False)
    release_date = serializers.DateField()
    price = serializers.IntegerField()
    author = serializers.CharField(max_length=30)
    reviews_quantity = serializers.IntegerField(default=0, read_only=True)
    rating = serializers.FloatField(min_value=0.0, max_value=10.0, default=0.0, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True, allow_null=True)

    class Meta:
        model = Book
        fields = "__all__"


# class FavouritesSerializer(serializers.Serializer):
#     book_id = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), required=False)
