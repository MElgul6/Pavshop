from django.db import models
from Blog.models import Category
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator,MinValueValidator

USER=get_user_model()


class Brand(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.title

class Property(models.Model):
    title = models.CharField(max_length=30)
    category = models.ManyToManyField(Category)

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.title


class PropertyValue(models.Model):
    title = models.CharField(max_length=30)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Property Value'
        verbose_name_plural = 'Property Values'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    designer = models.CharField(max_length=100) 
    property_value = models.ManyToManyField(PropertyValue)
    description = models.CharField(max_length=100)
    category=models.ForeignKey(Category,blank=True, related_name='product_category', on_delete=models.CASCADE)
    brands = models.ForeignKey(Brand, on_delete=models.CASCADE)
    main_image = models.ImageField(upload_to='media/Product', null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_new = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)

    
    def __str__(self):
        return self.title


class Discount(models.Model):
    value = models.IntegerField()
    is_percentage = models.BooleanField(default =  True)
    product = models.ManyToManyField(Product)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.value}'


class ProductImage(models.Model):
    product_image = models.ImageField(upload_to='media/Product')
    product = models.ForeignKey("Product", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product_image} {self.product}'


class Wish_list(models.Model):
    Product_id = models.ForeignKey("Product", on_delete=models.CASCADE)
   
    def __str__(self):
        return f'{self.Product_id}'
    
class Review(models.Model):
    author = models.ForeignKey(USER, on_delete=models.CASCADE, verbose_name='User',
                                        db_index=True,null=True,blank=True, related_name='reviewusers')
    rating=models.IntegerField(default=0, validators=[MaxValueValidator(5),MinValueValidator(0)])
    review_text = models.TextField()
    product = models.ForeignKey("Product",on_delete=models.CASCADE, related_name="reviews",null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.review_text}'



    

