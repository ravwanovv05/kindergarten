
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User
from accounts.serializers.RegisterSerializer import UserRegisterSerializer


class UserRegisterGenericAPIView(GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.validated_data['password'] != request.data.get('confirm_password'):
            return Response({'message': "Passwords don't match!"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=serializer.validated_data['username']).exists():
            return Response({'message': 'Username already exists!'}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

