from rest_framework import serializers

from .models import Profile, Favourite


class FavouriteSerializer(serializers.ModelSerializer):
    book_id = serializers.IntegerField()
    quantity = serializers.IntegerField()

    class Meta:
        model = Favourite
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.CharField()
    favourite = FavouriteSerializer(many=True)
    # subnotes = SubNoteSerializer(many=True, read_only=True)  # allow_null=True?

    class Meta:
        model = Profile
        fields = "__all__"
