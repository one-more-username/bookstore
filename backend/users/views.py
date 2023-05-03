from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import viewsets, generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from . import serializers
from .models import Profile
from .serializers import ProfileSerializer


User = get_user_model()

# Create your views here.


class ProfileViewSet(viewsets.ModelViewSet):
    # queryset = SubNote.objects.select_related("from_note")
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserRegistrationView(generics.ListCreateAPIView): #  ListCreateAPIView    TODO
    queryset = User.objects.all()
    permission_classes = (AllowAny, )
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


class UserLoginView(generics.RetrieveUpdateDestroyAPIView):  #  RetrieveUpdateDestroyAPIView TODO
    queryset = User.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = serializers.UserSerializer
