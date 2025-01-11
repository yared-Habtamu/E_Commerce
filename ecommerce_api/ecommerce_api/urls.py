"""
URL configuration for ecommerce_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('products.urls')),
#     # path('acc/',include('accounts.urls')),
# ]

from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token  # Import for Token Authentication
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView  # JWT Views


from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin Panel
    path('', include('products.urls')),  # Product App URLs
    path('api/jwt/login/', TokenObtainPairView.as_view(), name='jwt-login'),  # JWT Login
    path('api/jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
]