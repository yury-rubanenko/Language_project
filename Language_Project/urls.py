from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/profiles/', include('profiles.urls')),
    path('api/v1/platforms/', include('platforms.urls')),
]
