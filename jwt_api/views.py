from django.shortcuts import redirect
from django.views import View
from onelogin.saml2.auth import OneLogin_Saml2_Auth
from saml_settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from jwt_api.serializers import RegisterSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class HomeView(APIView):
    def get(self, request):
        return Response({"message" : "Welcome to the JWT API"})

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.validated_data['username'],
                                password=serializer.validated_data['password'])
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({
                        'access' : str(refresh.access_token),
                        'refresh' : str(refresh)
                    })
            return Response({"error" : "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SamlLoginView(APIView):
    def get(self, request):
        #this is where saml triggered you at login page
        return Response({"message" : "Redirect to SAML Identity Provider for authentication"})

class SamlACSView(APIView):
    def post(self, request):
        user_data = {
            'username' : request.data.get('username'),
            'first_name' : request.data.get('first_name'),
            'last_name' : request.data.get('last_name')
        }
        user, created = User.objects.get_or_create(username=user_data['username'])

        user.first_name = user_data['first_name']
        user.last_name = user_data['last_name']
        user.save()

        #Generate teh jwt token for this
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({
                'access' : access_token,
                'refresh' : str(refresh)
            })

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message" : "This is a protected view, you are protected"})

