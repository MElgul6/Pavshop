from django.db import models
from django.contrib.auth import get_user_model

USER=get_user_model()

class Category(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='./static/images/', null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'
        ordering=('-created_at','title')
    def __str__(self):
        return self.title

class Tag(models.Model):
    title=models.CharField(max_length=50)
    is_popular = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Blog(models.Model):
    title = models.CharField(max_length=50)
    image=models.ImageField(upload_to='./static/images/', null=True, blank=True)
    slug = models.SlugField('Slug', max_length=80, db_index=True)
    short_description=models.CharField(max_length=250)
    content=models.TextField()
    category = models.ForeignKey(Category, related_name='blogs', on_delete=models.CASCADE)
    price = models.IntegerField(null=True, blank=True)
    tags=models.ManyToManyField(Tag,blank=True, related_name='blog_tag')
    author=models.ForeignKey(USER,on_delete=models.CASCADE, null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(USER, on_delete=models.CASCADE, verbose_name='User',
                                        db_index=True,null=True,blank=True, related_name='comments')
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments",null=True,blank=True)