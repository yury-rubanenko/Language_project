from drf_yasg import openapi
from drf_yasg.views import get_schema_view


from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="api",
        default_version="v1",
        description="This API allows users to manage their learned words.",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

new_era =2
