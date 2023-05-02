from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'profile', ProfileViewSet)
router.register(r'favourite', FavouriteViewSet)

urlpatterns = []
urlpatterns += router.urls
