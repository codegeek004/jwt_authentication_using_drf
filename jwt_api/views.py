from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.serializers import 

#from docs
from rest_framework_simplejwt.serializers import TokenObtainPairViewSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework_simplejwt.tokens import RefreshTokens

class MyTokenObtainPairSerializer(TokenObtainPairViewSerializer):
	@classmethod
	def get_token(cls, user):
		token = super().get_token(user)

		#Add custom claims
		token['claims'] = user.name
		return token

class Home(APIView):
	authentication_classes = [JWTAuthentication]
	permission_classes = [IsAuthenticated]

	def get(self, request):
		content = {'message' : 'Hello World'}
		return Response(content)

def get_tokens_for_user(user):
	refresh = RefreshToken.for_user(user)

	return {
		'refresh' : str(refresh),
		'access' : str(refresh.access_token),
	}
