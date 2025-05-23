
from rest_framework import serializers
from accounts.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'phone_number', 'date_of_birth',
            'username', 'password', 'confirm_password', 'kindergarten',
            'role'
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)
        return user

