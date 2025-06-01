from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.permissions.Admin import AdminPermission
from main.models import Region, Kindergarten
from main.serializers.RegionSerializer import RegionSerializer, AddRegionsSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status


class RegionCreateAPIView(CreateAPIView):
    queryset = Region.objects.all()
    serializer_class = AddRegionsSerializer
    permission_classes = [AdminPermission, ]


class RegionListAPIView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [AdminPermission, ]


class RegionKindergartenCountView(APIView):
    def get(self, request, pk):

        region = get_object_or_404(Region, id=pk)


        count = Kindergarten.objects.filter(region_id=region.id).count()

        return Response({
            "pk": region.id,
            "region_title": region.title,
            "kindergarten_count": count
        }, status=status.HTTP_200_OK)
