from django.contrib.auth.models import User
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from demo.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio', ]


class UserSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):

    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'password', 'profile']

    def validate_password(self, value: str) -> str:

        return make_password(value)
