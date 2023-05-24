from django.db.models import Prefetch
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from books.models import Book
from users.models import Profile
from users.permissions import IsOwnerProfileOrReadOnly
from .models import ShoppingCart
from .serializers import ShoppingCartSerializer


# Create your views here.


class AddToShoppingCartView(generics.GenericAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'book_id'
    permission_classes = (IsOwnerProfileOrReadOnly, IsAuthenticated,)

    @extend_schema(
        summary='add to shopping cart for current user',
        tags=['shopping cart'],
        request=None,
        responses={200: {"Success": "Book added in shopping cart"}},
        parameters=[
            OpenApiParameter(
                name="book_id",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
        book = Book.objects.get(pk=kwargs['book_id'])
        profile = Profile.objects.get(user=request.user.id)

        shopping_cart = ShoppingCart.objects.get(owner=profile)
        shopping_cart.books_to_purchase.add(book)

        return Response({"Success": "Book added in shopping cart"}, status=status.HTTP_200_OK)


class RemoveFromShoppingCartView(generics.GenericAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'book_id'
    permission_classes = (IsOwnerProfileOrReadOnly, IsAuthenticated,)

    @extend_schema(
        summary='remove from shopping cart for current user',
        tags=['shopping cart'],
        request=None,
        responses={200: {"Success": "Book removed from shopping cart"}},
        parameters=[
            OpenApiParameter(
                name="book_id",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
        book = Book.objects.get(pk=kwargs['book_id'])
        profile = Profile.objects.get(user=request.user.id)

        shopping_cart = ShoppingCart.objects.get(owner=profile)
        shopping_cart.books_to_purchase.remove(book)

        return Response(self.get_serializer(shopping_cart).data, status=status.HTTP_200_OK)


class GetShoppingCartView(generics.GenericAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
    permission_classes = (IsOwnerProfileOrReadOnly, IsAuthenticated,)

    @extend_schema(
        summary='get shopping cart for current user',
        tags=['shopping cart'],
        request=None,
        responses={200: ShoppingCartSerializer},
    )
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user.id)

        shopping_cart = ShoppingCart.objects.get(owner=profile)

        return Response(self.get_serializer(shopping_cart).data, status=status.HTTP_200_OK)


class MakePurchaseView(generics.GenericAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
    permission_classes = (IsOwnerProfileOrReadOnly, IsAuthenticated,)

    @extend_schema(
        summary='make a purchase',
        tags=['shopping cart'],
        request=None,
        responses={200: {'Success': 'Purchase completed'}},
    )
    def get(self, request, *args, **kwargs):
        shopping_cart = ShoppingCart.objects.get(owner=request.user.id)

        books_to_purchase = shopping_cart.books_to_purchase.all()
        purchase_history = shopping_cart.owner.purchase_history.all()

        shopping_cart.owner.purchase_history.set(books_to_purchase | purchase_history)
        shopping_cart.books_to_purchase.clear()

        return Response({'Success': 'Purchase completed'}, status=status.HTTP_200_OK)
