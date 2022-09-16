
from django.template import Library
from Core.forms import SubscriberForm
from Core.models import Subscriber
from django.contrib import messages
from Blog.models import Tag
from Product.models import Category, Product

register=Library()

@register.simple_tag
def get_subscriber(request):
    form=SubscriberForm()
    if request.method == 'POST':
        form = SubscriberForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ugurla subscribe olundu')
            
    context={
        'form': form
    }
    return context

@register.simple_tag
def get_populars_tag():
   tags = Tag.objects.filter(is_popular = True)
   return tags





    
