from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'user_profile', views.UserProfileViewSet, basename='user-profile')

urlpatterns = [
    path('', include(router.urls)),
]
