from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.permissions.Admin import Admin
from main.models import Region, Kindergarten
from main.serializers.RegionSerializer import RegionSerializer, AddRegionsSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status


class RegionCreateAPIView(CreateAPIView):
    queryset = Region.objects.all()
    serializer_class = AddRegionsSerializer
    permission_classes = [Admin, ]


class RegionListAPIView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [Admin, ]


class RegionKindergartenCountView(APIView):
    def get(self, request, pk):

        region = get_object_or_404(Region, id=pk)

        descendants = region.get_descendants(include_self=True)

        count = Kindergarten.objects.filter(region__in=descendants).count()

        return Response({
            "pk": region.id,
            "region_title": region.title,
            "kindergarten_count": count
        }, status=status.HTTP_200_OK)
