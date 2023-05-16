from django.urls import path

from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'book', BookViewSet)

urlpatterns = [
    path('book/random/', RandomBooksView.as_view()),
    path('book/favourites/', FavouritesView.as_view()),
    path('book/<int:book_id>/add-favourite/', AddFavouritesView.as_view()),
    path('book/<int:book_id>/remove-favourite/', RemoveFavouritesView.as_view()),
    path('book/<int:book_id>/add-review/', AddReviewView.as_view()),
    path('book/search/<str:title>/', BookSearchView.as_view())
    # path('book/<int:book_id>/reviews/', BookReviewsView.as_view()),
]
urlpatterns += router.urls
