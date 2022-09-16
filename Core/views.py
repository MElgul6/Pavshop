from django.shortcuts import redirect, render
from Product.models import Discount, Product, Category, PropertyValue, Review
from Core.forms import ContactForm,SubscriberForm
from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from Core.models import Contact

def about(request):
    return render(request,'about-us.html')

def index(request): 
    new_products = Product.objects.all().order_by('-id')[:8]
    popular_products = Product.objects.annotate(nreview=Count('reviews')).order_by("-nreview")[:8]
    context = {
        'new_products':  new_products,
        'popular_products': popular_products,
        }
        
    return render(request,'index.html', context)


# class CoreView(IndexView):
#     model=Product
#     context_object_name='homepage'
#     template_name='index.html'

#     def get_context_data(self, **kwargs):
#         context = super(CoreView, self).get_context_data(**kwargs)
#         context['product'] = Product.objects.all()[:8]
#         return context



@login_required
def contact(request):
    form=ContactForm()
   
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('contact'))
        
    context={
        'form': form
    }
   
    return render(request,'contact.html',context)



class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('about')

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, _('Mesajiniz qebul olundu'))
        return super().get_success_url()


def subscribe(request):
    form=SubscriberForm()
    if request.method == 'POST':
        form = SubscriberForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('contact'))
    context={
        'form': form
    }
    return render(request,'footer.html',context)
