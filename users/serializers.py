from rest_framework import serializers
from .models import User, Survey # Changed UserSurvey to Survey

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'date_joined')
        read_only_fields = ('id', 'date_joined')

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'confirm_password', 'first_name', 'last_name')

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords don't match")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(
            # username=validated_data['email'], # username is optional now
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user

class SurveySerializer(serializers.ModelSerializer): # Was UserSurveySerializer
    class Meta:
        model = Survey # Changed from UserSurvey
        fields = '__all__' # Or list specific fields
        read_only_fields = ('id', 'created_at')

    def validate_age(self, value):
        if value < 15 or value > 65: # Adjusted age range, modify as needed
            raise serializers.ValidationError("Age must be between 15 and 65 years")
        return value

class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    subject = serializers.CharField(max_length=200)
    message = serializers.CharField()

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email is required")
        return value

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()