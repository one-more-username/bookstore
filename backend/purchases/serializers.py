from rest_framework import serializers

from .models import ShoppingCart
from books.serializers import BookSerializer


class ShoppingCartSerializer(serializers.ModelSerializer):
    # owner = serializers.CharField(max_length=30)
    owner = serializers.ReadOnlyField()
    books_to_purchase = BookSerializer(many=True)

    class Meta:
        model = ShoppingCart
        fields = "__all__"
