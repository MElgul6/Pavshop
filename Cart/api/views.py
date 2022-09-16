# from http.client import HTTPResponse
from django.http import HttpResponse
from itertools import product
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.response import Response
from rest_framework import status
from Cart.api.serializers import CartItemSerializer,CartCreateSerializer,CartSerializer
# ,CartItemOrderSerializer,CartSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from Cart.models import CartItem,Cart
from Product.models import Product
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


class GenericAPIViewSerializerMixin:

    def get_serializer_class(self):
        return self.serializer_classes[self.request.method] 

class CartItemDeleteView(GenericAPIViewSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_classes = {
        'DELETE': CartCreateSerializer,
        'PATCH': CartCreateSerializer,
    }

class CartUpdateView(GenericAPIViewSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_classes = {
        'PATCH': CartSerializer,
    }

class CartItemAPI(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request,*args, **kwargs):
        items = CartItem.objects.all()
        serializer=CartItemSerializer(items, context={'request': request}, many=True)
        return JsonResponse(serializer.data, safe=False)

    
    def post(self, request, *args, **kwargs):
        form_data = request.data
        print('start')
        basket, created = Cart.objects.get_or_create(user = request.user, status=False)
        
        if created is True:
           
            qty=request.data['quantity']
            form_data['quantity']=qty
            serializer = CartCreateSerializer(data=form_data, context={'request': request})
            
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, safe=False, status=201)
            return JsonResponse(serializer.errors, safe=False, status=400)
        else:
            
            if CartItem.objects.filter(product=request.data['product'],cart=basket.id).exists():
                
                cartitem=CartItem.objects.filter(product=request.data['product'],cart=basket.id).first()
                qty=cartitem.quantity+int(request.data['quantity'])
                CartItem.objects.filter(product=request.data['product'], cart=basket.id).update(quantity=qty)
                ty=CartItem.objects.filter(cart=basket.id)
                posts = CartCreateSerializer(ty, many=True).data
                print('end')
                return JsonResponse(posts,safe=False, status=200)
            
            else:
                print(request.data)
                qty=request.data['quantity']
                form_data['quantity']=qty
                
                print('back')
                serializer = CartCreateSerializer(data=form_data, context={'request': request})
                
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, safe=False, status=201)
                return JsonResponse(serializer.errors, safe=False, status=400)

 