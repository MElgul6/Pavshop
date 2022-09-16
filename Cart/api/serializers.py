from django.db.models import Sum
from rest_framework import serializers
from Cart.models import CartItem,Cart
from Product.models import Product
from Product.api.serializers import ProductSerializer

class CartSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Cart
        fields = (
            'id',
            'user',
            'status')

    def validate(self, data):
        request = self.context['request']
        data['user'] = request.user
        return super().validate(data)


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer() 
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    sub_total = serializers.SerializerMethodField()
    cart=CartSerializer()
    class Meta:
        model = CartItem
        fields = (
            'id',
            'user',
            'quantity',
            'total_price',
            'product',
            'cart',
            'sub_total'
        )

    def get_sub_total(self, obj):
        subtotal=0
        items=obj.cart.cart_items.all()
        for item in items:
            subtotal+=item.total_price
        return subtotal
   

    def create(self, validated_data):
        request = self.context.get('request')
        basket, created = Cart.objects.get_or_create(user = request.user, status=False)
        validated_data['cart'] = basket
        return super().create(validated_data)

    def get_total_price(self,instance):
        return instance.total_price()

    def validate(self, data):
        request = self.context['request']
        data['user'] = request.user
        return super().validate(data)


class CartCreateSerializer(serializers.ModelSerializer):
    # cart=serializers.PrimaryKeyRelatedField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    sub_total = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = (
            'id',
            'user',
            'quantity',
            'product',
            'get_price',
            'get_image',
            'get_title',
            'total_price',
            'sub_total',
            'cart',
            'created_at'           
        )
    
    def get_sub_total(self, obj):
        subtotal=0
        items=obj.cart.cart_items.all()
        
        for item in items:
            subtotal+=item.total_price
        return subtotal
 
    def create(self, validated_data):
        request = self.context.get('request')
       
        basket, created = Cart.objects.get_or_create(user = request.user, status=False)
        print(created)
        validated_data['cart'] = basket
        return super().create(validated_data)


    def get_total_price(self,instance):
        return instance.total_price()
    
    def get_get_price(self,instance):
        return instance.get_price()
    
    def get_get_image(self,instance):
        return instance.get_image()
    
    def get_get_title(self,instance):
        return instance.get_title()

    def validate(self, data):
        request = self.context['request']
        data['user'] = request.user
        return super().validate(data)


# class CartItemOrderSerializer(serializers.ModelSerializer):
#     user = serializers.PrimaryKeyRelatedField(read_only=True)
#     class Meta:
#         model = CartItem
#         fields = (
#             'id',
#             'user',
#             'quantity',
#             'total_price'
#         )
#     def get_total_price(self,instance):
#         return instance.total_price()

#     def validate(self, data):
#         request = self.context['request']
#         data['user'] = request.user
#         return super().validate(data)



