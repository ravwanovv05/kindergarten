from rest_framework import serializers
from accounts.models import User
from rest_framework.serializers import ModelSerializer


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
            'password': {
                'write_only': True
            }
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):

        validated_data.pop('confirm_password', None)
        return User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            date_of_birth=validated_data['date_of_birth'],
            username=validated_data['username'],
            password=validated_data['password'],
            kindergarten=validated_data['kindergarten'],
            role=validated_data['role']
        )


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'phone_number', 'date_of_birth',
            'username', 'kindergarten', 'role'
        )
