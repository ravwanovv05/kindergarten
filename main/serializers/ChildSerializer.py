from os import pread

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from main.models import Child


class AddChildSerializer(ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'
        read_only_fields = ('id',)


class ChildListSerializer(ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'


class ChildDetailSerializer(ModelSerializer):
    full_name = serializers.SerializerMethodField()
    parent_full_name = serializers.SerializerMethodField()
    parent_phone_number = serializers.CharField(source='parent_id.phone_number', read_only=True)
    payment_status_display = serializers.SerializerMethodField()

    class Meta:
        model = Child
        fields = (
            'id',
            'full_name',
            'parent_full_name',
            'parent_phone_number',
            'payment_status_display',
        )

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    def get_parent_full_name(self, obj):
        parent = obj.parent_id
        if parent:
            return f"{parent.first_name} {parent.last_name}"
        return None

    def get_payment_status_display(self, obj):
        return "To'langan" if obj.payment_status else "To'lanmagan"
