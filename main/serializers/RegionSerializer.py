from rest_framework.serializers import ModelSerializer

from main.models import Region


class AddRegionsSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = ('title',)

class RegionSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'