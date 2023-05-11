from random import sample

from django.conf import settings
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.response import Response

from users.models import Profile
from users.permissions import IsOwnerProfileOrReadOnly
from users.serializers import ProfileSerializer, FavouritesSerializer
from .models import Book, Review
from .serializers import BookSerializer, ReviewSerializer


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


class AddFavouritesView(generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsOwnerProfileOrReadOnly, IsAuthenticated, )

    @extend_schema(
        summary='add to favourites for current user',
        tags=['favourites'],
        request=None,
        responses={200: ProfileSerializer},
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

        book = Book.objects.get(pk=params['book_id'])

        profile = Profile.objects.get(user=request.user.id)

        profile.favourites.add(book)
        profile.save()

        # s_params = FavouritesSerializer(data=params)
        #
        # profile = Profile.objects.filter(user=request.user.id)
        #
        # if s_params.is_valid(raise_exception=True):
        #     book_id = s_params.validated_data['book_id'].id
        #
        #     if book_id is not None:
        #         book = Book.objects.get(pk=book_id)
        #         s_book = BookSerializer(data=book)
        #
        #         # if s_book.is_valid(raise_exception=True):
        #         #     print("BOOK", s_book.data)
        #
        #         profile[0].favourites.add(book)
        #         # profile.save()

        return Response(self.get_serializer(profile).data)


class RemoveFavouritesView(generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsOwnerProfileOrReadOnly, IsAuthenticated, )

    @extend_schema(
        summary='remove from favourites for current user',
        tags=['favourites'],
        request=None,
        responses={200: ProfileSerializer},
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
        print("BOOK_ID", params['book_id'])
        # book = Book.objects.get(pk=params['book_id'])

        profile = Profile.objects.get(user=request.user.id)

        # profile.favourites.add(book)
        # profile.save()
        print("FAVOURITES", profile.favourites)

        # for item in favourites:
        #     if item['id'] == params['book_id']:
        #         # remove book from favourites
        #         return Response()

        return Response(self.get_serializer(profile).data)
