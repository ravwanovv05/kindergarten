from django.urls import path
from accounts.views.users import UserRegisterGenericAPIView, UserInfo, RoleCount
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('authorization/register', UserRegisterGenericAPIView.as_view(), name='register'),
    path('authorization/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('authorization/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('user-info', UserInfo.as_view(), name='user_info'),
    path('role-count/', RoleCount.as_view(), name='role_count'),
]