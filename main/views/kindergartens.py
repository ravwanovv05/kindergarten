from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from main.serializers.kindergartens import KindergartenSerializer


class AddKindergartenGenericAPIView(GenericAPIView):
    serializer_class = KindergartenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)