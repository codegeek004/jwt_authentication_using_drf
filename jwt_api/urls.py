from django.urls import path
from jwt_api.views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
	path('auth/api/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/api/refresh', TokenRefreshView.as_view(), name='token_refresh_view'),
	path('register/', RegisterView.as_view(), name="user-registration"),

]