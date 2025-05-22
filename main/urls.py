from django.urls import path
from main.views.districts import AddDistrictGenericAPIView
from main.views.kindergartens import AddKindergartenGenericAPIView
from main.views.regions import AddRegionGenericAPIView

urlpatterns = [
    path('region/add-region', AddRegionGenericAPIView.as_view(), name='add_region'),
    path('region/add-district', AddDistrictGenericAPIView.as_view(), name='add_district'),
    path('kindergarten/add-kindergarten', AddKindergartenGenericAPIView.as_view(), name='add_kindergarten'),
]
