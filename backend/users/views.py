from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from .models import Profile, Favourite
from .serializers import ProfileSerializer, FavouriteSerializer


# Create your views here.

class ProfileViewSet(viewsets.ModelViewSet):
    # queryset = SubNote.objects.select_related("from_note")
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    # permission_classes = (IsAdminUser, )
    # permission_classes = (IsAdminOrReadOnly, )


class FavouriteViewSet(viewsets.ModelViewSet):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
    # permission_classes
