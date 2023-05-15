from random import sample

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.response import Response

from users.models import Profile
from users.permissions import IsOwnerProfileOrReadOnly
from users.serializers import ProfileSerializer
from .models import Book, Review
from .serializers import BookSerializer, ReviewSerializer


# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class RandomBooksView(generics.ListAPIView):
    books = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):
        books = Book.objects.all()
        random_books = sample(self.get_serializer(books, many=True).data, 10)
        return Response(random_books)


class AddReviewView(generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'book_id'
    permission_classes = (IsOwnerProfileOrReadOnly, IsAuthenticated,)

    @extend_schema(
        summary='add review for the book',
        tags=['reviews'],
        request=ReviewSerializer,
        responses={200: {"Success": "Review added"}},
        parameters=[
            OpenApiParameter(
                name="book_id",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH
            ),
        ],
    )
    def post(self, request, *args, **kwargs):

        book = Book.objects.get(pk=kwargs['book_id'])

        review = Review(
            author=request.user,
            book=book,
            review=request.data['review'],
            rating=request.data['rating'],
        )
        review.save()

        return Response({"Success": "Review added"}, status=status.HTTP_200_OK)


class FavouritesView(generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsOwnerProfileOrReadOnly, IsAuthenticated,)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(profile__user=self.request.user.id)

    @extend_schema(
        methods=['get'],
        summary='get favourites for current user',
        tags=['favourites'],
        request=None,
        responses={200: ProfileSerializer},
    )
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user.id)

        return Response(self.get_serializer(profile).data)


class AddFavouritesView(generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'book_id'
    permission_classes = (IsOwnerProfileOrReadOnly, IsAuthenticated,)

    @extend_schema(
        summary='add to favourites for current user',
        tags=['favourites'],
        request=None,
        responses={200: ProfileSerializer},
        parameters=[
            OpenApiParameter(
                name="book_id",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
        book = self.get_object()
        profile = Profile.objects.get(user=request.user.id)

        profile.favourites.add(book)

        return Response({"Success": "Book added in favourites"}, status=status.HTTP_200_OK)


class RemoveFavouritesView(generics.GenericAPIView):
    queryset = Book.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'book_id'
    serializer_class = ProfileSerializer
    permission_classes = (IsOwnerProfileOrReadOnly, IsAuthenticated,)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(profile__user=self.request.user.id)

    @extend_schema(
        summary='remove from favourites for current user',
        tags=['favourites'],
        request=None,
        responses={200: ProfileSerializer},
        parameters=[
            OpenApiParameter(
                name="book_id",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
        book = self.get_object()
        profile = Profile.objects.get(user=request.user.id)

        profile.favourites.remove(book)

        return Response({"Success": "Book removed from favourites"}, status=status.HTTP_200_OK)
