from django.urls import path
from main.views.DistrictsView import AddDistrictGenericAPIView
from main.views.KindergartenView import KindergartenListAPIView, KindergartenCreateAPIView, KindergartenSearchAPIView, \
    RegionDistrictKindergartenListView
from main.views.RegionView import RegionCreateAPIView, RegionListAPIView, RegionKindergartenCountView

urlpatterns = [
    path('region/add-district', AddDistrictGenericAPIView.as_view(), name='add_district'),
    path('add-kindergarten/', KindergartenCreateAPIView.as_view(), name='add_kindergarten'),
    path('list-kinderkarten/', KindergartenListAPIView.as_view(), name='list_kinderkarten'),
    path('add-region/', RegionCreateAPIView.as_view(), name='add_region'),
    path('region-list/', RegionListAPIView.as_view(), name='region_list'),
    path('region/<int:pk>/kindergarten/', RegionKindergartenCountView.as_view(), name='kindergarten_count'),
    path('search-kindergarten/', KindergartenSearchAPIView.as_view(), name='search_kindergarten'),
    path('region/<int:region_id>/district/<int:district_id>/kindergartens/',
         RegionDistrictKindergartenListView.as_view(), name='region-district-kindergartens'),
]
