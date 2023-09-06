from django.contrib import admin
from django.urls import path, include, re_path
from .swagger_settings import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('profiles.urls')),
    path('api/v1/platforms/', include('platforms.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
