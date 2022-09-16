from django.contrib import admin
# from .models import Product,Product_image,Wish_list,Review
from modeltranslation.admin import TranslationAdmin
from .models import Product, ProductImage, Wish_list, Review, Property, PropertyValue, Brand, Discount

admin.site.register([Product, ProductImage, Wish_list, Review, Property, PropertyValue, Brand, Discount])


     
