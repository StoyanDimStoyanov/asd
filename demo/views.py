import views as views
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import views as rest_views
from rest_framework.response import Response
# Create your views here.
from rest_framework import generics

from demo.serializers import UserSerializer


class UserDetailsApiView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class UserDetailsApiView(rest_views.APIView):
#
#     def get(self, req):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
#
#     def post(self,req):
#
