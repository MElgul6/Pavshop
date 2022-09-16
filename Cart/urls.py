from django.urls import path
from Cart.views import checkout,shopping,updateItem



urlpatterns = [
    path('cart/',shopping,name="shopping"),
    path('checkout/',checkout,name="checkout"),
    path('updatecartitem/',updateItem, name="updatecartitem"),
        
]

