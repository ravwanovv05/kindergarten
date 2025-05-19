from rest_framework_simplejwt.views import TokenObtainPairView

from accounts.serializers.LoginSerializer import PhoneLoginSerializer


class PhoneLoginView(TokenObtainPairView):
    serializer_class = PhoneLoginSerializer
