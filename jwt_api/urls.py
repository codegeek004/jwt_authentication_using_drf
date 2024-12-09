from django.urls import path
from jwt_api.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
	path('register/', RegisterView.as_view(), name="register"),
	path('login/', LoginView.as_view(), name="login"),
	path('protected/', ProtectedView.as_view(), name="protected"),
	path('', HomeView.as_view(), name="home")

]