from rest_framework import serializers

from .models import Book, Review


class ReviewSerializer(serializers.ModelSerializer):
    # book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review = serializers.CharField(max_length=255)
    author = serializers.ReadOnlyField(default=serializers.CurrentUserDefault())
    rating = serializers.IntegerField(max_value=10, min_value=1)

    class Meta:
        model = Review
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=255)
    image = serializers.ImageField(required=False)
    release_date = serializers.DateField()
    price = serializers.IntegerField()
    author = serializers.CharField(max_length=30)
    reviews_quantity = serializers.IntegerField(default=0, read_only=True)
    rating = serializers.FloatField(min_value=0.0, max_value=10.0, default=0.0, read_only=True)
    # reviews = ReviewSerializer(many=True, read_only=True, allow_null=True)

    class Meta:
        model = Book
        fields = "__all__"
