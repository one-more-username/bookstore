from rest_framework import serializers

from .models import ShoppingCart, BookForBuy


class BookForBuySerializer(serializers.ModelSerializer):
    book_id = serializers.IntegerField()
    quantity = serializers.IntegerField()

    class Meta:
        model = BookForBuy
        fields = "__all__"


class ShoppingCartSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(max_length=30)
    book_for_buy = BookForBuySerializer(many=True)
    # subnotes = SubNoteSerializer(many=True, read_only=True)  # allow_null=True?

    class Meta:
        model = ShoppingCart
        fields = "__all__"
