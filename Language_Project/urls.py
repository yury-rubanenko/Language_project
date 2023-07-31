from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Підключення URL-шляхів profiles
    path('profiles/', include('profiles.urls')),
]
