from django.urls import path

from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
# router.register(r'shopping_cart', ShoppingCartViewSet)

urlpatterns = [
    path('shopping-cart/add-book/<int:book_id>/', AddToShoppingCartView.as_view()),
    # path('shopping-cart/remove-book/<int:book_id>/', RemoveFromShoppingView.as_view()),
    # path('shopping-cart/', ShoppingCartView.as_view()),
    # path('shopping-cart/buy/', ShoppingCartBuyView.as_view())
]
urlpatterns += router.urls
