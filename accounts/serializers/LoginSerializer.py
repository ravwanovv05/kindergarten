from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()


class PhoneLoginSerializer(TokenObtainPairSerializer):
    username_field = 'phone_number'

    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        phone = attrs.get("phone_number")
        password = attrs.get("password")

        try:
            user = User.objects.get(phone_number=phone)
        except User.DoesNotExist:
            raise serializers.ValidationError("Noto‘g‘ri telefon raqam yoki parol")


        auth_user = authenticate(username=user.username, password=password)
        if not auth_user:
            raise serializers.ValidationError("Noto‘g‘ri telefon raqam yoki parol")


        data = super().validate({
            "username": user.username,
            "password": password
        })

        return data
