from django.urls import path

from .views import *
from rest_framework import routers

router = routers.SimpleRouter()

urlpatterns = [
    path("profile/registration/", UserRegistrationView.as_view()),
]

urlpatterns += router.urls
