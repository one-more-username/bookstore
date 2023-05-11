from random import sample

from django.conf import settings
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.response import Response

from users.models import Profile
from users.permissions import IsOwnerProfileOrReadOnly
from users.serializers import ProfileSerializer
from .models import Book, Review
from .serializers import BookSerializer, ReviewSerializer, FavouritesSerializer


# Create your views here.
# class GetRandomBooksView(views.APIView):
# random_object = Book.objects.order_by('?')[0]
# or
# products = list(Book.objects.all())
# products = random.sample(products, 10)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # @action(methods=['get'], detail=False, url_path='get-random-books')
    # def get_random_books(self, *args, **kwargs):
    #     books = Book.objects.all()
    #     random_books = sample(self.get_serializer(books, many=True).data, 10)
    #     return Response(random_books)


class RandomBooksView(generics.ListAPIView):
    books = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):
        books = Book.objects.all()
        random_books = sample(self.get_serializer(books, many=True).data, 10)
        return Response(random_books)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes


class FavouritesView(generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer = FavouritesSerializer
    permission_classes = (IsOwnerProfileOrReadOnly, IsAuthenticated,)

    @extend_schema(
        methods=['get'],
        summary='get favourites for current user',
        tags=['favourites'],
        request=None,
        responses={200: ProfileSerializer},
    )
    def get(self, request, *args, **kwargs):
        serializer_class = FavouritesSerializer

        profile = Profile.objects.filter(user=settings.AUTH_USER_MODEL)

        profile.favourites += request.data['favourites']['book_id']
        # profile.save()

        return Response(serializer_class(profile.favourites).data)

        # owner = request.user.id
        # books = Book.objects.all()

        # book_id = self.serializer(request.data.book_id, many=False)
        # return Response(book_id.data)


class AddFavouritesView(generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer = FavouritesSerializer
    permission_classes = (IsOwnerProfileOrReadOnly, IsAuthenticated, )

    @extend_schema(
        summary='add to favourites for current user',
        tags=['favourites'],
        request=None,
        responses={200: FavouritesSerializer},
        parameters=[
            OpenApiParameter(
                name="book_id",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                # required=False
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
        params = request.query_params
        s_params = FavouritesSerializer(data=params)

        profile = Profile.objects.filter(user=request.user.id)

        if s_params.is_valid(raise_exception=True):
            book_id = s_params.validated_data['book_id'].id
            print("BOOK_ID", book_id)

            if book_id is not None:
                book = Book.objects.filter(id=book_id)
                # print("fadsf", book)
                s_book = BookSerializer(data={
                    "title": book[0].title,
                    "description": book[0].description,
                    # "image": book[0].image,
                    "release_date": book[0].release_date,
                    "price": book[0].price,
                    "author": book[0].author,
                    "reviews_quantity": book[0].reviews_quantity
                })
                if s_book.is_valid(raise_exception=True):
                    print("S_BOOK_DATA", s_book.validated_data)
                s_favourites = []
                favourites = profile[0].favourites.all()

                # profile[0].favourites = favourites
                # profile.save()

        # profile.favourites += request.data['book_id']
        # profile.save()

        return Response(ProfileSerializer(profile, many=True).data)


class RemoveFavouritesView(generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer = FavouritesSerializer
    permission_classes = (IsOwnerProfileOrReadOnly, IsAuthenticated,)

    @extend_schema(
        summary='remove from favourites for current user',
        tags=['favourites'],
        request=None,
        responses={200: FavouritesSerializer},
    )
    def get(self, request, *args, **kwargs):
        serializer_class = FavouritesSerializer

        profile = Profile.objects.filter(user=settings.AUTH_USER_MODEL)

        profile.favourites += request.data['favourites']['book_id']
        # profile.save()

        return Response(serializer_class(profile.favourites).data)
