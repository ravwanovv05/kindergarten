from django.urls import path

from main.views.kindergarten import KindergartenCreateAPIView, KindergartenListAPIView, KindergartenUpdateAPIView

urlpatterns = [
    path('kindergarten/', KindergartenCreateAPIView.as_view(), name='kindergarten-create'),
    path('kindergarten-list/', KindergartenListAPIView.as_view(), name='kindergarten-list'),
    path('update-kindergarten/', KindergartenUpdateAPIView.as_view(), name='kindergarten-update'),
]