from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from accounts.views.Login import PhoneLoginView
from accounts.views.Register import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('Login/', PhoneLoginView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]