from django.urls import path
from accounts.views.users import UserRegisterGenericAPIView, LogoutGenericAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('auth/register', UserRegisterGenericAPIView.as_view(), name='register'),
    path('auth/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/logout', LogoutGenericAPIView.as_view(), name='logout')
]