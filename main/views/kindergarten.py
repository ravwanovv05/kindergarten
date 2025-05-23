from django.core.exceptions import PermissionDenied
from requests.models import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from main.models import Kindergarten
from main.serializers.KindergartenSerializer import KindergartenSerializer, KindergartenListSerializers


class KindergartenCreateAPIView(CreateAPIView):
    serializer_class = KindergartenSerializer
    # permission_classes = (IsAuthenticated,)


class KindergartenListAPIView(ListAPIView):
    queryset = Kindergarten.objects.all()
    serializer_class = KindergartenListSerializers
    # permission_classes = (IsAuthenticated,)


class KindergartenUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = KindergartenSerializer
    # permission_classes = (IsAuthenticated,)

    def get_object(self):
        user = self.request.user
        if user.role != 'director':
            raise PermissionDenied
        return user.kindergarten

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Bog‘cha o‘chirildi'}, status=status.HTTP_204_NO_CONTENT)
