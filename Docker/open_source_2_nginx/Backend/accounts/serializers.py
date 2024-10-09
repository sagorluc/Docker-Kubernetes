from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    password         = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    
    class Meta:
        model        = User
        fields       = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'password'        : {'write_only': True},
            'confirm_password': {'write_only': True}
        }
        
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username is already taken.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already registered.")
        return value

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        if len(data['password']) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return data
    
    
    def create(self, validate_data):
        # Remove  confirm_password that we dont't need anymore
        password = validate_data.pop('password')
        validate_data.pop('confirm_password')
        
        # Create a new user and set password
        user = User.objects.create(**validate_data)
        user.set_password(password)
        user.save()
        
        Token.objects.create(user=user)
        return user
    


        