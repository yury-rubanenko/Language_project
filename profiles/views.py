from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer

class UserProfileView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(pk=user.pk)