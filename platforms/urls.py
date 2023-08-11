from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views 


router = DefaultRouter()
router.register('my-words', views.UserWordsListView, basename='user-words') 
router.register(r'words', views.WordListView, basename='word')

urlpatterns = [
    path('', include(router.urls)),
]

