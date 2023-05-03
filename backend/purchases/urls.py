from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'shopping_cart', ShoppingCartViewSet)

urlpatterns = router.urls
