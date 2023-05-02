from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'profile', ShoppingCartViewSet)
router.register(r'favourite', BookForBuyViewSet)

urlpatterns = []
urlpatterns += router.urls
