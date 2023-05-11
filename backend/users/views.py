from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import viewsets, generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from . import serializers
from .models import Profile
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import ProfileSerializer


User = get_user_model()

# Create your views here.


class ProfileViewSet(viewsets.ModelViewSet):
    # queryset = SubNote.objects.select_related("from_note")
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsOwnerProfileOrReadOnly, IsAuthenticated, )


class UserRegistrationView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.UserSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
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
        user.refresh_from_db()
        sr_user = serializers.UserSerializer(user)

        return Response(sr_user.data, status=status.HTTP_201_CREATED)

    # def perform_create(self, serializer):
    #     user = self.request.user
    #     serializer.save(user=user)


class UserLoginView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (IsOwnerProfileOrReadOnly, IsAuthenticated, )
    serializer_class = serializers.UserSerializer


# class AddToFavouriteView(generics.UpdateAPIView):
#     queryset = Profile.objects.all()
#     permission_classes = (IsOwnerProfileOrReadOnly, IsAuthenticated, )
#     serializer_class = serializers.ProfileSerializer
#
#     def partial_update(self, request, *args, **kwargs):
#         kwargs['partial'] = True
#         return self.update(request, *args, **kwargs)

