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
