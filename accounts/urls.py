from django.urls import path
from accounts.views.users import UserRegisterGenericAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('authorization/register', UserRegisterGenericAPIView.as_view(), name='register'),
    path('authorization/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('authorization/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]