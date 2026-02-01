from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Vote

class VoteRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['identity', 'dob', 'phone']  # Adjust fields to match your Vote model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        return user

