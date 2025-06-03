from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from main.models import Group


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ('title', 'number_of_children', 'nursery_id', 'kindergarten_id',)
        read_only_fields = ('created_at',)
