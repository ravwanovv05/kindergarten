from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from accounts.models import User
from main.models import Kindergarten


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number']

class KindergartenSerializer(serializers.ModelSerializer):
    director = serializers.SerializerMethodField()

    class Meta:
        model = Kindergarten
        fields = ['id', 'title', 'number_of_children', 'director']

    def get_director(self, obj):
        director = User.objects.filter(kindergarten=obj, role='director').first()
        if director:
            return DirectorSerializer(director).data
        return None


class KindergartenListSerializers(ModelSerializer):
    class Meta:
        model = Kindergarten
        fields = '__all__'




