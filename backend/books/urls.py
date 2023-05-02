from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'book', BookViewSet)
router.register(r'review', ReviewViewSet)

urlpatterns = []
urlpatterns += router.urls
