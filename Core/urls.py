from django.urls import path
from Core.views import contact,index,about

urlpatterns = [
    path('',about, name='about'),
    path('contact/',contact, name="contact"),
    path('index/',index, name="homepage"),
       
 ]
