from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from books.models import Book
from users.models import Profile
from users.permissions import IsOwnerProfileOrReadOnly
from .models import ShoppingCart
from .serializers import ShoppingCartSerializer


# Create your views here.

# class ShoppingCartViewSet(viewsets.ModelViewSet):
#     queryset = ShoppingCart.objects.all()
#     serializer_class = ShoppingCartSerializer
#     permission_classes = (IsOwnerProfileOrReadOnly, IsAuthenticated, )


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
        responses={200: ShoppingCartSerializer},
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


# class UserRegistrationView(generics.GenericAPIView):
#     queryset = User.objects.all()
#     permission_classes = (AllowAny, )
#     serializer_class = UserRegistrationSerializer
#
#     @transaction.atomic  # does it need at decorator extended schema?
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         user = User(
#             username=serializer.validated_data['username']
#         )
#         user.set_password(serializer.validated_data['password'])
#         user.save()
#
#         profile = Profile(
#             user=user,
#         )
#         profile.save()
#
#         profile.refresh_from_db()
#         shopping_cart = ShoppingCart(
#             owner=profile,
#         )
#         shopping_cart.save()
#
#         user.refresh_from_db()
#         sr_user = UserRegistrationSerializer(user)
#
#         return Response(sr_user.data, status=status.HTTP_201_CREATED)
