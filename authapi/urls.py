from django.urls import path
from authapi.views import *
urlpatterns = [
    path('register/', UserRegistration.as_view(), name='Register'),
]
