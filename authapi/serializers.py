from django.core.exceptions import ValidationError
from rest_framework import serializers
from authapi.models import models
from authapi.models import User

#for sending a password reset link to email
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from authapi.utils import Util


#serializer for user registration
class UserRegistrationSerializer(serializers.ModelSerializer):
	#additional field for user during registration
	password2 = serializers.CharField(style={'input_type' : 'password'}, write_only=True)
	class Meta:
		model = User 
		fields = ['email', 'name', 'password', 'password2', 'tc']
		extra_kwargs = {
			'password' : {'write_only' : True}
		}
	#custom validation for password and confirm password
	def validate(self, attrs):   #data comes from view in attrs in this function
		password = attrs.get('password')
		password2 = attrs.get('password2')
		if password != password2:
			raise serializers.ValidationError('Password and confirm passwords does not match')
		return attrs

	def create(self, validate_data):
		return User.objects.create_user(**validate_data)


class UserLoginSerializer(serializers.ModelSerializer):
	email = serializers.EmailField(max_length=200)
	class Meta:
		model = User 
		fields = ['email', 'password']
