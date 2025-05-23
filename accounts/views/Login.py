from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.serializers.LoginSerializer import UsernameLoginSerializer

class UsernameLoginView(TokenObtainPairView):
    serializer_class = UsernameLoginSerializer
