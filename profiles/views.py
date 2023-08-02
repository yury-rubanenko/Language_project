from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Дозвіл для авторизованих користувачів
def user_profile(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)