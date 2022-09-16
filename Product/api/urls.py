from django.urls import path
from Product.api.views import ProductAPI, ProductDetail


urlpatterns  = [
    path('products/', ProductAPI.as_view(), name="api_products"),
    path('products/<int:pk>/', ProductDetail.as_view (), name="api_products"), 

]