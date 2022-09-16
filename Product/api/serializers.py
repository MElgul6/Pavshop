from dataclasses import field, fields
from unicodedata import category
from rest_framework import serializers
from Product.models import Product, Category, Brand


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'title',
            'image',
            'created_at',
            'updated_at',
            
        )


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'title',
            'created_at',
            'updated_at',
            
        )


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    brands = BrandSerializer()
    class Meta:
        model = Product
        
        fields = (
            'id',
            'title',
            'price',
            'designer',
            'description',
            'main_image',
            'category',
            'brands',
            'created_at',
            'updated_at',
        )

class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'title',
            'price',
            'designer',
            'description',
            'main_image',
            'category',
            'brands',
        )