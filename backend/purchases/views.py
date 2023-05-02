from rest_framework import viewsets

from .models import ShoppingCart, BookForBuy
from .serializers import ShoppingCartSerializer, BookForBuySerializer


# Create your views here.

class ShoppingCartViewSet(viewsets.ModelViewSet):
    # queryset = SubNote.objects.select_related("from_note")
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
    # permission_classes


class BookForBuyViewSet(viewsets.ModelViewSet):
    queryset = BookForBuy.objects.all()
    serializer_class = BookForBuySerializer
    # permission_classes
