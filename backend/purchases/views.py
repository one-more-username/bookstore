from rest_framework import viewsets

from .models import ShoppingCart
from .serializers import ShoppingCartSerializer


# Create your views here.

class ShoppingCartViewSet(viewsets.ModelViewSet):
    # queryset = SubNote.objects.select_related("from_note")
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
    # permission_classes
