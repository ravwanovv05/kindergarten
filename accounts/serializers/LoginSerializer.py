from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class UsernameLoginSerializer(TokenObtainPairSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("Noto‘g‘ri username yoki parol")

        # Super chaqirish JWT token olish uchun
        data = super().validate({
            "username": username,
            "password": password
        })
        return data
