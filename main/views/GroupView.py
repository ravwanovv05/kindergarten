from requests.models import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView

from accounts.permissions.Admin import AdminPermission
from main.models import Group, Child
from main.serializers.ChildSerializer import ChildListSerializer
from main.serializers.GroupSerializer import GroupSerializer


class CreateGroupAPIView(CreateAPIView):
    queryset = Group.objects.all()
    permission_classes = [AdminPermission, ]
    serializer_class = GroupSerializer

class GroupChildrenListAPIView(ListAPIView):
    permission_classes = [AdminPermission, ]
    serializer_class = ChildListSerializer
    def get_queryset(self):
        group_id = self.kwargs['pk']
        return Child.objects.filter(group_id=group_id)

class GroupListAPIView(ListAPIView):
    queryset = Group.objects.all()
    permission_classes = [AdminPermission, ]
    serializer_class = GroupSerializer