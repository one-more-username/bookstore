from django.urls import path

from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
# router.register(r'shopping_cart', ShoppingCartViewSet)

urlpatterns = [
    path('shopping-cart/add-book/<int:book_id>/', AddToShoppingCartView.as_view()),
    # todo: need validation for existing books in shopping cart
    path('shopping-cart/remove-book/<int:book_id>/', RemoveFromShoppingCartView.as_view()),
    path('shopping-cart/', GetShoppingCartView.as_view()),
    path('shopping-cart/buy/', MakePurchaseView.as_view())
]
urlpatterns += router.urls
