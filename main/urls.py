from django.urls import path

from main.views.ChildView import AddChildAPIView, ChildCountAPIView, ChildListAPIView, ChildSearchAPIView, \
    ChildDetailAPIView
from main.views.DistrictsView import AddDistrictGenericAPIView
from main.views.GroupView import CreateGroupAPIView, GroupChildrenListAPIView, GroupListAPIView
from main.views.KindergartenView import KindergartenListAPIView, KindergartenCreateAPIView, KindergartenSearchAPIView, \
    RegionDistrictKindergartenListView, KindergartenPaymentCreateAPIView, KindergartenStatisticsAPIView
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
    path('add-group/', CreateGroupAPIView.as_view(), name='add_group'),
    path('payment-kindergarten/', KindergartenPaymentCreateAPIView.as_view(), name='kindergarten_payment'),
    path('add-child/', AddChildAPIView.as_view(), name='add_child'),
    path('child-count/', ChildCountAPIView.as_view(), name='child_count'),
    path('list-child/', ChildListAPIView.as_view(), name='child_list'),
    path('search-child/', ChildSearchAPIView.as_view(), name='search_child'),
    path('groups/<int:pk>/children/', GroupChildrenListAPIView.as_view(), name='group-children-list'),
    path('list-groups/', GroupListAPIView.as_view(), name='group_list'),
    path('children/<int:pk>/', ChildDetailAPIView.as_view(), name='child-detail'),
    path('kindergartens/<int:pk>/statistics/', KindergartenStatisticsAPIView.as_view(), name='kindergarten-statistics'),
]
