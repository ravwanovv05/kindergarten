from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
import datetime
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


class KindergartenPaymentSerializer(serializers.ModelSerializer):
    payment = serializers.SerializerMethodField()

    class Meta:
        model = Kindergarten
        fields = ('id', 'payment',)

        def get_payment(self, obj):
            now = datetime.datetime.now()
            payments = obj.payments.filter(data__year=now.year, data__mont=now.month)
            if payments.exists():
                total_paid = sum(p.amount for p in payments)
                expected_paid = obj.expected_monthly_payment
                if expected_paid > 0:
                    percent = int((total_paid / expected_paid) * 100)
                    return f"{percent}"
                return "0%"
