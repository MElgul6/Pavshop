from django.contrib import admin
from .models import  Tag, Comment, Blog, Category


admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Blog)
admin.site.register(Category)
