import  time
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from celery import shared_task
from Core.models import Subscriber
from Product.models import Product
from django.db.models import Count
from datetime import datetime,timedelta
from django.contrib.auth import get_user_model

User=get_user_model()

@shared_task
def send_mail_to_subscribers():
    email_list = Subscriber.objects.filter(is_active=True)\
        .values_list('email', flat=True)
    product = Product.objects.all()

    message = render_to_string('email-subscribers.html', {
                'product': product
            })
    subject = 'New blog from out website'
    mail = EmailMultiAlternatives(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=email_list)
    start_date = datetime.now() - timedelta(hours=4,minutes=40)
    end_time = datetime.now()
    products = Product.objects.filter(created_at__range=(start_date, end_time)).annotate(nreview=Count('reviews')).order_by("-nreview")[:3]
    mail.content_subtype = 'html'
    mail.send()


@shared_task
def send_mail_to_subscribers_leyla():
    start_date = datetime.now() - timedelta(30)
    end_time = datetime.now()
    users = User.objects.filter(last_login = (start_date, end_time))
    email_list=[]
    for user in users:
        email_list.append(user.email)
    product = Product.objects.all()
    message = render_to_string('email-subscribers.html', {
                'product': product
            })
    subject = 'New blog from out website'
    mail = EmailMultiAlternatives(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=email_list)
    
    products = Product.objects.filter(created_at__range=(start_date, end_time)).annotate(nreview=Count('reviews')).order_by("-nreview")[:5]
    
    mail.content_subtype = 'html'
    mail.send()
