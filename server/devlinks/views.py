from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer

# Create your views here.
class UserCreateAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
