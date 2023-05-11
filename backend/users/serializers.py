from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from books.models import Book
from books.serializers import BookSerializer
from .models import Profile

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password2',
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs


class FavouritesSerializer(serializers.Serializer):
    book_id = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), required=False)


class ProfileSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # favourites = FavouritesSerializer(many=True)
    favourites = BookSerializer(many=True)

    class Meta:
        model = Profile
        fields = ("favourites", )

