from django.urls import path

from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'profile', ProfileViewSet)

urlpatterns = [path('registration', UserRegistrationView.as_view()), ]  #   change it TODO
# urlpatterns = [path('login', UserLoginView.as_view(), name="login"), ]
# urlpatterns = [path('logout', UserLogoutView.as_view(), name="logout"), ]
urlpatterns += router.urls
