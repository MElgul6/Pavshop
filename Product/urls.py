from django.urls import path
from Product.views import (
    list,
    like_product_view, 
    ProductListView,
    ProductDetailView
)

urlpatterns = [
    path('products/', ProductListView.as_view(), name="products"),
    path('products/<int:pk>/', ProductDetailView.as_view(), name="product-detail"),
    path('like-product/<int:id>/', like_product_view, name = 'like_product'),
 ]
