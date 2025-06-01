from django.urls import path

from main.views.KindergartenView import KindergartenCreateAPIView, KindergartenListAPIView, KindergartenUpdateAPIView
from main.views.RegionView import RegionCreateAPIView, RegionListAPIView, RegionKindergartenCountView

urlpatterns = [
    path('kindergarten/', KindergartenCreateAPIView.as_view(), name='kindergarten-create'),
    path('kindergarten-list/', KindergartenListAPIView.as_view(), name='kindergarten-list'),
    path('update-kindergarten/', KindergartenUpdateAPIView.as_view(), name='kindergarten-update'),
    path('add-region/', RegionCreateAPIView.as_view(), name='region-create'),
    path('region-list/', RegionListAPIView.as_view(), name='region-list'),
    path('region/<int:pk>/kindergarten-count/', RegionKindergartenCountView.as_view(), name='region_kindergarten_count'),
]