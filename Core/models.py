from django.db import models
from django.db import models
from email import contentmanager
from django.db import models
from django.contrib.auth import get_user_model
USER=get_user_model()

class Contact(models.Model):
    fullname=models.CharField('FULL NAME *', max_length=50)
    email=models.EmailField('EMAIL *', max_length=50)
    phone =models.CharField('PHONE *', max_length=10)
    subject=models.CharField(max_length=150)
    message =models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Subscriber(models.Model):
    email=models.EmailField(max_length=50)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
class Team(models.Model):
    fullname=models.CharField(max_length=50)
    job_title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='./static/images/')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


