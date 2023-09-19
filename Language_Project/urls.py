from django.contrib import admin
from django.urls import include, path, re_path
from allauth.account.views import (
    LoginView, 
    LogoutView, 
    SignupView,
    PasswordChangeView,
)
from .swagger_settings import schema_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/login/", LoginView.as_view(), name="account_login"),
    path("accounts/logout/", LogoutView.as_view(), name="account_logout"),
    path("accounts/signup/", SignupView.as_view(), name="account_signup"),
    path("accounts/password/change/", PasswordChangeView.as_view(), name="account_change_password"),
    path("api/v1/users/", include("profiles.urls")),
    path("api/v1/platforms/", include("platforms.urls")),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
]
