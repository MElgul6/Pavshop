from rest_framework.views import APIView
from Product.models import Product
from rest_framework import status
from Product.api.serializers import (
    ProductSerializer,ProductCreateSerializer
)
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

class ProductAPI(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        product = Product.objects.all()
        serializer = ProductSerializer(product, context={'request': request},many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        form_data = request.data
        serializer = ProductCreateSerializer(data=form_data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status=201)
        return JsonResponse(serializer.errors, safe=False, status=400)

class ProductDetail(APIView):

    def put(self,request,pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(instance=product, data = request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)


    def get_object(self, pk):
        if self.request.method == "GET":
            try:
                return Product.objects.get(pk=pk)
            except Product.DoesNotExist:
                raise JsonResponse(status=status.HTTP_404_NOT_FOUND)
        
 







