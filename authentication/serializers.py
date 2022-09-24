# using git commit -m
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)
    number_phone = serializers.CharField(max_length=255, min_length=2)
    address = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'number_phone', 'address']

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(validated_data)
