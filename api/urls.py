from django.urls import path
from .views import main, UserCreateView, UserDetailView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('', main, name='main'),
    path('register/', UserCreateView.as_view(), name='api-register'),
    path('profile/', UserDetailView.as_view(), name='api-profile'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]