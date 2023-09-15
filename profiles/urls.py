from django.urls import path

from . import views

urlpatterns = [
    path(r"user_profile/", views.UserProfileViewSet.as_view({"get": "list"}), name="user-profile"),
]
