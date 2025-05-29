from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from accounts.permissions.Admin import Admin
from main.models import Region
from main.serializers.RegionSerializer import RegionSerializer, AddRegionsSerializer


class RegionCreateAPIView(CreateAPIView):
    queryset = Region.objects.all()
    serializer_class = AddRegionsSerializer
    permission_classes = [Admin,]


class RegionListAPIView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [Admin, ]

