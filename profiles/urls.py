from django.urls import path
from . import views

urlpatterns = [
    # URL-шлях для сторінки профілю користувача
    path('profile/', views.user_profile, name='user_profile'),
]
