from django.urls import path
from .views import WordImportView

urlpatterns = [
    path('import-words/', WordImportView.as_view(), name='import-words'),
]