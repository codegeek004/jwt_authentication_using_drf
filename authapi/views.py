from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from authapi.serializers import UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth import authenticate
from authapi.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

#Generate token manually using RefreshToken for a user
def get_tokens_for_user(user):
	refresh = RefreshToken.for_user(user)

	return {
		'refresh' : str(refresh),
		'access' : str(refresh.access_token),
	}

#Define view for user registration
class UserRegistration(APIView):
	renderer_classes = [UserRenderer]
	def post(self, request, format=None):
		#create a user serializer instance
		serializer = UserRegistrationSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.save()
			token = get_tokens_for_user(user)
			return Response({'token':token, 'msg':'Registration successful'}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
	renderer_classes = [UserRenderer]
	def post(self, request, format=None):
		serializer = UserLoginSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			email = serializer.data.get('email')
			password = serializer.data.get('password')
			user = authenticate(email=email, password=password)
			if user is None:
				token = get_tokens_for_user(user)
				return Response({'token':token, 'msg':'Registration successful'}, status=status.HTTP_200_OK)
			else:
				return Response({'errors': {'non_field_errors' : ['Email or Password is not valid']}}, status=status.HTTP_404_NOT_FOUND)







