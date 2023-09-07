from rest_framework import serializers

from django.contrib.auth import get_user_model
from authemail.serializers import SignupSerializer, LoginSerializer

User = get_user_model()


class UserProfileSignupSerializer(SignupSerializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'password2')


class UserProfileLoginSerializer(LoginSerializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'password')
