from rest_framework import serializers
from main.models import Kindergarten


class KindergartenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kindergarten
        fields = '__all__'

