
from itertools import product
from re import T
from statistics import mode
from django.db import models
from Product.models import Product
from User.models import User
from django.contrib.auth import get_user_model

USER=get_user_model()

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', related_name='cart_items', on_delete=models.CASCADE, )
    product =  models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE, null=True)
    # order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        total = self.product.price * self.quantity
        return total

    @property
    def get_price(self):
        price= self.product.price
        return price

    @property
    def get_image(self):
        image= self.product.main_image.url
        return image

    @property
    def get_title(self):
        title= self.product.title
        return title


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    # created_at=models.DateTimeField(auto_now_add=True)
    # updated_at=models.DateTimeField(auto_now=True)

    @property
    def cart_total(self):
        subtotal=0
        items=self.cart_items.all()
        for item in items:
            subtotal+=item.total_price
        # orderitems = self.cartitem.all()
        # subtotal = sum([item.total_price for item in orderitems])
        return subtotal

class Billing_details(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    company=models.CharField(max_length=30)
    address=models.CharField(max_length=150)
    city=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    phone =models.CharField(max_length=10)
    author=models.ForeignKey(USER,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Shipping_info(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    company=models.CharField(max_length=30)
    address=models.CharField(max_length=150)
    city=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    phone =models.CharField(max_length=10)
    author=models.ForeignKey(USER,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


