from rest_framework.serializers import ModelSerializer

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
            'kindergarten',  # <-- To‘g‘risi shu
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            date_of_birth=validated_data['date_of_birth'],
            role=validated_data['role'],
            kindergarten=validated_data['kindergarten'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
