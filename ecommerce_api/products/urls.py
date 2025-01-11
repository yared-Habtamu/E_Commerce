from django.urls import path
from . import views

urlpatterns = [
    path('api/products/', views.ProductListCreateView.as_view(), name='product-list'),
    path('api/products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('api/reviews/', views.ReviewListCreateView.as_view(), name='review-list-create'),
    path('api/cart/', views.CartListCreateView.as_view(), name='cart-list-create'),
    path('api/orders/', views.OrderListCreateView.as_view(), name='order-list-create'),
    path('',views.home,name='home'),
    path('/products',views.product_list, name='product_list'),
]