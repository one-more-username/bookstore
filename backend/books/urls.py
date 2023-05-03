from django.urls import include, path

from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'book', BookViewSet)
router.register(r'review', ReviewViewSet)

urlpatterns = router.urls
# urlpatterns = [
#     path('book/', BookViewSet.as_view({
#         'get': 'retrieve',
#         'put': 'update',
#         'patch': 'partial_update',
#         'delete': 'destroy'
#     })),
#     path('review/', ReviewViewSet.as_view({
#         'get': 'retrieve',
#         'put': 'update',
#         'patch': 'partial_update',
#         'delete': 'destroy'
#     })),
# ]
