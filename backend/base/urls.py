from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from . import views

urlpatterns = [
    path('users/login/', views.MyTokenObtainPairView.as_view(),
     name='token_obtain_pair'),
    path('', views.getRoutes, name='routes'),
    path('users/profile/', views.getUserProfile, name='users-profile'),
    path('products/', views.getProducts, name='products'),
    path('products/<str:pk>', views.getProduct, name='product'),
]