from django.urls import path

from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'profile', ProfileViewSet)

urlpatterns = []
# urlpatterns = [path('registration', UserRegistrationView.as_view()), ]
# gets all user profiles and create a new profile
path("all-profiles", UserRegistrationView.as_view(), name="all-profiles"),
# retrieves profile details of the currently logged in user
path("profile/<int:pk>", UserLoginView.as_view(), name="profile"),

urlpatterns += router.urls
