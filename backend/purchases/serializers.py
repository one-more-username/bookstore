from rest_framework import serializers

from users.serializers import ProfileSerializer
from .models import ShoppingCart
from books.serializers import BookSerializer


class ShoppingCartSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(read_only=True)
    books_to_purchase = BookSerializer(many=True)

    class Meta:
        model = ShoppingCart
        fields = "__all__"
        # todo: validation for existing books in shopping cart
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Review.objects.all(),
        #         fields=['author', 'book']
        #     )
        # ]
