from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from main.models import Region
from main.serializers.regions import RegionSerializer


class AddRegionGenericAPIView(GenericAPIView):
    serializer_class = RegionSerializer

    def get_queryset(self):
        return Region.objects.all()


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
