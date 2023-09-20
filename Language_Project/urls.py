from django.contrib import admin
from django.urls import include, path, re_path
from allauth.account.views import SignupView, LoginView, PasswordChangeView, PasswordResetView, LogoutView, EmailView
from allauth.socialaccount import views as socialaccount_views
from .swagger_settings import schema_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('signup/', SignupView.as_view(), name='account_signup'),
    path('login/', LoginView.as_view(), name='account_login'),
    path('logout/', LogoutView.as_view(), name='account_logout'),
    path('google/signup/', socialaccount_views.SignupView.as_view(), name='google_signup'),
    path('password/change/', PasswordChangeView.as_view(), name='account_change_password'),
    path('password/reset/', PasswordResetView.as_view(), name='account_reset_password'),
    path('accounts/email/', EmailView.as_view(), name='account_email'),
    path("api/v1/users/", include("profiles.urls")),
    path("api/v1/platforms/", include("platforms.urls")),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
]
