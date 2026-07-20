from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    """Serializer for Account model"""
    class Meta:
        model = Account
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'bio', 'profile_picture', 'created_at']
        read_only_fields = ['id', 'created_at']


class SignupSerializer(serializers.ModelSerializer):
    """Serializer for user signup"""
    password = serializers.CharField(write_only=True, min_length=6)
    password_confirm = serializers.CharField(write_only=True, min_length=6)
    
    class Meta:
        model = Account
        fields = ['username', 'email', 'password', 'password_confirm', 'first_name', 'last_name']
    
    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data
    
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        password = validated_data.pop('password')
        user = Account(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    """Serializer for user login"""
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
