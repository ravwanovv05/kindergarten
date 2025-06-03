from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView

from accounts.permissions.Admin import AdminPermission
from main.models import Kindergarten, Region, District
from main.serializers.KindergartenSerializer import KindergartenSerializer, KindergartenListSerializers, \
    KindergartenPaymentSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models.functions import TruncDay, TruncMonth, TruncYear
from django.db.models import Sum, Count
from datetime import datetime

from main.models import Kindergarten, Payment


class KindergartenCreateAPIView(CreateAPIView):
    serializer_class = KindergartenSerializer
    permission_classes = (AdminPermission,)


class KindergartenListAPIView(ListAPIView):
    queryset = Kindergarten.objects.all()
    serializer_class = KindergartenListSerializers
    permission_classes = [AdminPermission, ]


class KindergartenUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = KindergartenSerializer
    permission_classes = AdminPermission

    def get_object(self):
        user = self.request.user
        if user.role != 'director':
            raise PermissionDenied
        return user.kindergarten

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Bog‘cha o‘chirildi'}, status=status.HTTP_204_NO_CONTENT)


class KindergartenSearchAPIView(ListAPIView):
    queryset = Kindergarten.objects.all()
    serializer_class = KindergartenSerializer
    permission_classes = [AdminPermission, ]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title']


class RegionDistrictKindergartenListView(APIView):
    def get(self, request, region_id, district_id):
        region = get_object_or_404(Region, id=region_id)
        district = get_object_or_404(District, id=district_id, region_id=region.id)

        kindergartens = Kindergarten.objects.filter(district_id=district.id)

        serializer = KindergartenListSerializers(kindergartens, many=True)

        return Response({
            "region_id": region.id,
            "region_title": region.title,
            "district_id": district.id,
            "district_title": district.title,
            "kindergartens": serializer.data
        }, status=status.HTTP_200_OK)


class KindergartenPaymentCreateAPIView(CreateAPIView):
    serializer_class = KindergartenPaymentSerializer
    permission_classes = (AdminPermission,)


class KindergartenStatisticsAPIView(APIView):
    def get(self, request, pk):
        period = request.query_params.get('period', 'monthly').lower()
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if period not in ['daily', 'monthly', 'yearly']:
            return Response({"error": "Invalid period. Choose from daily, monthly, yearly."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            kindergarten = Kindergarten.objects.get(pk=pk)
        except Kindergarten.DoesNotExist:
            return Response({"error": "Kindergarten not found."}, status=status.HTTP_404_NOT_FOUND)

        payments = Payment.objects.filter(kindergarten_id=kindergarten)

        # Sana bo‘yicha filter
        if start_date:
            try:
                start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
                payments = payments.filter(added_at__date__gte=start_date_obj)
            except ValueError:
                return Response({"error": "Invalid start_date format. Use YYYY-MM-DD"},
                                status=status.HTTP_400_BAD_REQUEST)

        if end_date:
            try:
                end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
                payments = payments.filter(added_at__date__lte=end_date_obj)
            except ValueError:
                return Response({"error": "Invalid end_date format. Use YYYY-MM-DD"},
                                status=status.HTTP_400_BAD_REQUEST)

        # Period bo‘yicha guruhlash
        if period == 'daily':
            payments = payments.annotate(period=TruncDay('added_at'))
        elif period == 'monthly':
            payments = payments.annotate(period=TruncMonth('added_at'))
        else:  # yearly
            payments = payments.annotate(period=TruncYear('added_at'))

        stats = payments.values('period').annotate(
            total_amount=Sum('amount'),
            total_payments=Count('id')
        ).order_by('period')

        # Response tayyorlash
        data = [
            {
                "period": stat['period'].strftime('%Y-%m-%d'),
                "total_amount": stat['total_amount'],
                "total_payments": stat['total_payments']
            }
            for stat in stats
        ]

        return Response({
            "kindergarten_id": pk,
            "period": period,
            "statistics": data
        })
