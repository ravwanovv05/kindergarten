from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from main.models import Kindergarten



class KindergartenSerializer(ModelSerializer):
    class Meta:
        model = Kindergarten
        fields = '__all__'
        read_only_fields = ('id',)


class KindergartenListSerializers(ModelSerializer):
    class Meta:
        model = Kindergarten
        fields = '__all__'




