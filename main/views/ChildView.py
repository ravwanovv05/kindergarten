from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from accounts.permissions.Admin import AdminPermission
from main.models import Child
from main.serializers.ChildSerializer import AddChildSerializer, ChildListSerializer, ChildDetailSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter

class AddChildAPIView(CreateAPIView):
    permission_classes = (AdminPermission,)
    serializer_class = AddChildSerializer


class ChildCountAPIView(APIView):
    permission_classes = (AdminPermission,)

    def get(self, request):
        child_count = Child.objects.count()
        return Response({'child_count': child_count})


class ChildListAPIView(ListAPIView):
    queryset = Child.objects.all()
    permission_classes = (AdminPermission,)
    serializer_class = ChildListSerializer



class ChildSearchAPIView(ListAPIView):
    queryset = Child.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChildListSerializer
    filter_backends = (SearchFilter,)
    search_fields = ['first_name', 'last_name', 'parent_id__phone_number']


class ChildDetailAPIView(RetrieveAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildDetailSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'pk'