from django.urls import path
from . import views 

urlpatterns = [
    path(r'<str:language_slag>/words/', views.WordListView.as_view(), name='words-list'),
    path(r'<str:language_slag>/my-words/', views.UserWordsListView.as_view(), name='user-words-list'),
    path(r'<str:language_slag>/my-words/<int:pk>/update/', views.UpdateUserWordsAPIView.as_view(), name='user-words-update'),
    path(r'<str:language_slag>/my-words/<int:pk>/delete/', views.DeleteUserWordsAPIView.as_view(), name='user-words-delete'),
]
