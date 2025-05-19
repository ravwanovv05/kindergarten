from rest_framework.serializers import ModelSerializer, ValidationError
from django.contrib.auth.password_validation import validate_password
from accounts.models.users import User


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'phone_number',
            'date_of_birth',
            'password',
            'role',
            'kindergarten',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise ValidationError("This username is already taken.")
        return value

    def validate_password(self, value):
        validate_password(value)  # Django default password validators
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
