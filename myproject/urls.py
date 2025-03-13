from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('jwt_api.urls')),
    path('api/auth/', include('jwt_api.urls')),]
