from django.urls import include, path

from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'book', BookViewSet)
router.register(r'review', ReviewViewSet)

urlpatterns = [
    path('book/random/', RandomBooksView.as_view()),
    path('book/favourites/', FavouritesView.as_view()),
    path('book/favourites/add/', AddFavouritesView.as_view()),
    path('book/favourites/remove/<int:book_id>', RemoveFavouritesView.as_view()),
]
urlpatterns += router.urls
