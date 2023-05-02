from django.shortcuts import render
from rest_framework import viewsets

from .models import Book, Review
from .serializers import BookSerializer, ReviewSerializer


# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    # queryset = SubNote.objects.select_related("from_note")
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes
