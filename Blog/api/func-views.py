from rest_framework.views import APIView
from Blog.models import Category,Blog
from Blog.api.serializers import (
    BlogReadSerializer, 
    # BlogCreateSerializer, 
    CategorySerializer, CategoryCreateSerializer
)
from django.http import JsonResponse


class CategoryAPI(APIView):

    def get(self, request,*args, **kwargs):
        categories = Category.objects.all()
        serializer=CategorySerializer(categories, context={'request': request}, many=True)
        return JsonResponse(serializer.data, safe=False)


    def post(self, request, *args, **kwargs):
        form_data = request.data
        serializer = CategoryCreateSerializer(data=form_data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status=201)
        return JsonResponse(serializer.errors, safe=False, status=400)


class CategoryUpdateDeleteAPI(APIView):

    def put(self,request, *args, **kwargs):
        id = kwargs['pk']
        category = Category.objects.get(id=id)
        category_data = request.data
        serializer = CategoryCreateSerializer(data=category_data, instance=category)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, safe=False, status=200)
    
    def patch(self,request, *args, **kwargs):
        id = kwargs['pk']
        category = Category.objects.get(id=id)
        category_data = request.data
        serializer = CategoryCreateSerializer(data=category_data, partial=True, instance=category)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, safe=False, status=200)
    




class BlogAPI(APIView):
    def get(self, request,*args, **kwargs):
        blogs = Blog.objects.all()
        serializer=BlogReadSerializer(blogs, context={'request': request}, many=True)
        return JsonResponse(serializer.data, safe=False) 