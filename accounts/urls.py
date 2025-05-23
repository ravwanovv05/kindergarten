from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from accounts.views.Login import UsernameLoginView
from accounts.views.Register import UserRegisterGenericAPIView
from accounts.views.UserInfo import UserInfoAPIView
from accounts.views.UserList import UserListAPIView

urlpatterns = [
    path('Register/', UserRegisterGenericAPIView.as_view(), name='register'),
    path('login/', UsernameLoginView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('User-info/', UserInfoAPIView.as_view(), name='user_info'),
    path('user-list/', UserListAPIView.as_view(), name='user_list'),
]