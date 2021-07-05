from django.contrib.auth.models import User
from rest_framework import generics, status
from demo.serializers import UserSerializer


class UserDetailsApiView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
