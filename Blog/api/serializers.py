from requests import request
from rest_framework import serializers
from Blog.models import Blog
from Product.models import Category


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            'id',
            'title',
            'short_description',
            'image',
            'category',
            'created_at',
            'updated_at',
        )


class CategoryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'image'
        )


class CategorySerializer(serializers.ModelSerializer):
    blogs = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'image',
            'blogs'
        )
    
    def get_blogs(self, obj):
        serializer = BlogCategorySerializer(obj.blogs.all(), context=self.context, many=True)
        return serializer.data


class BlogReadSerializer(serializers.ModelSerializer):
    author=serializers.PrimaryKeyRelatedField(read_only=True)
    category = CategorySerializer()

    class Meta:
        model = Blog
        fields = (
            'id',
            'title',
            'short_description',
            'image',
            'author',
            'category',
            'created_at',
            'updated_at',
        )

    def validate(self, data):
        request=self.context['request']
        data['author']= request.user
        return super().validate(data)


class BlogCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = (
            'id',
            'title',
            'short_description',
            'image',
            'author',
            'category',
        )


