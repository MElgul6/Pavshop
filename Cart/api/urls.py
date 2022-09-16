from django.urls import path
from Cart.api.views import CartItemAPI, CartItemDeleteView,CartUpdateView
# ,CartAPI


urlpatterns = [
    # path('addcart/', CartItemViews.as_view(), name='api_cart'),
    path('order/<int:pk>/', CartUpdateView.as_view()),
    path('cart/', CartItemAPI.as_view()),
    path('cart/<int:pk>/', CartItemDeleteView.as_view(), name="api_cart"),
   
]