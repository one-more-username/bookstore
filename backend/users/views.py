from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from purchases.models import ShoppingCart
from .models import Profile
from .serializers import UserRegistrationSerializer

User = get_user_model()

# Create your views here.


class UserRegistrationView(generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = UserRegistrationSerializer

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User(
            username=serializer.validated_data['username']
        )
        user.set_password(serializer.validated_data['password'])
        user.save()

        profile = Profile(
            user=user,
        )
        profile.save()

        profile.refresh_from_db()
        shopping_cart = ShoppingCart(
            owner=profile,
        )
        shopping_cart.save()

        user.refresh_from_db()
        sr_user = UserRegistrationSerializer(user)

        return Response(sr_user.data, status=status.HTTP_201_CREATED)
