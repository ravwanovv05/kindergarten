from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from accounts.models import User
from accounts.serializers.users import UserRegisterSerializer, LogoutSerializer


class UserRegisterGenericAPIView(GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']
        confirm_password = request.data['confirm_password']

        if User.objects.filter(username=username).exists():
            return Response({'message': 'Username already exists!'})

        if password != confirm_password:
            return Response({'message': "Passwords don't match!"})

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LogoutGenericAPIView(GenericAPIView):
    serializer_class = LogoutSerializer

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
