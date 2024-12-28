from django.urls import path
from . import views

urlpatterns = [
    path('api/products/', views.ProductListCreateView.as_view(), name='product-list'),
    path('api/products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('', views.product_list, name='product_list'),
]