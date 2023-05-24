from django.urls import path

from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
# router.register(r'profile', ProfileViewSet)

urlpatterns = [
    # path('registration/', UserRegistrationView.as_view()),
    # gets all user profiles and create a new profile
    path("profile/registration/", UserRegistrationView.as_view()),
    # retrieves profile details of the currently logged in user
    # path("profile/authentication/", UserAuthenticationView.as_view()),
]

urlpatterns += router.urls
