from rest_framework import serializers
from accounts.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'phone_number', 'date_of_birth',
            'username', 'password', 'confirm_password', 'kindergarten_id'
        )

        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        return User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            date_of_birth=validated_data['date_of_birth'],
            username=validated_data['username'],
            password=validated_data['password'],
            kindergarten_id=validated_data['kindergarten_id']
        )
