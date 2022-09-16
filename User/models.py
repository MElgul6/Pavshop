from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_("email address"), blank=True, unique=True)
    bio = models.TextField('Bio', null=True, blank=True)
    image = models.ImageField('Image', upload_to='user_images/')
    phone = models.CharField('Phone number', max_length=15)
    adress = models.CharField('Adress', max_length=100)
    country = models.CharField('Country', max_length=50)
    city = models.CharField('Town/City', max_length=50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    @property
    def profile_picture(self):
        if self.image:
            return self.image

    def __str__(self):
        return self.email