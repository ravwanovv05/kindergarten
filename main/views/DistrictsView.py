from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from main.models import District
from main.serializers.districts import DistrictSerializer


class AddDistrictGenericAPIView(GenericAPIView):
    serializer_class = DistrictSerializer

    def get_queryset(self):
        return District.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
