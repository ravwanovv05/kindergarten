from rest_framework.generics import ListAPIView

from accounts.models import User
from accounts.permissions.Admin import Admin
from accounts.serializers.UserSerializer import UserSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (Admin,)