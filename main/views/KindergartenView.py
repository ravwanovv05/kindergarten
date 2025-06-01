from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView

from accounts.permissions.Admin import AdminPermission
from main.models import Kindergarten, Region, District
from main.serializers.KindergartenSerializer import KindergartenSerializer, KindergartenListSerializers


class KindergartenCreateAPIView(CreateAPIView):
    serializer_class = KindergartenSerializer
    permission_classes = (AdminPermission,)


class KindergartenListAPIView(ListAPIView):
    queryset = Kindergarten.objects.all()
    serializer_class = KindergartenListSerializers
    permission_classes = [AdminPermission, ]


class KindergartenUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = KindergartenSerializer
    permission_classes = AdminPermission

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


class KindergartenSearchAPIView(ListAPIView):
    queryset = Kindergarten.objects.all()
    serializer_class = KindergartenSerializer
    permission_classes = [AdminPermission, ]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title']



class RegionDistrictKindergartenListView(APIView):
    def get(self, request, region_id, district_id):
        region = get_object_or_404(Region, id=region_id)
        district = get_object_or_404(District, id=district_id, region_id=region.id)

        kindergartens = Kindergarten.objects.filter(district_id=district.id)

        serializer = KindergartenListSerializers(kindergartens, many=True)

        return Response({
            "region_id": region.id,
            "region_title": region.title,
            "district_id": district.id,
            "district_title": district.title,
            "kindergartens": serializer.data
        }, status=status.HTTP_200_OK)