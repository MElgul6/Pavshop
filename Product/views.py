
from os import stat
from django.shortcuts import render,redirect
from django.http import HttpResponse
from Product.forms import ReviewForm
from Product.models import Discount, Product, Category, PropertyValue, Review,Brand
from Cart.models import CartItem,Cart
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView
from Blog.models import Tag
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from django.db.models import Count


def like_product_view(request,id):
    request.session['liked_products']=f"{request.session.get('liked_products','')}{id}," 
    messages.success(request, 'Product like edildi')
    return redirect(reverse_lazy('products'))


def list(request):
    # l_products = list(map(int,request.session.get('liked_products','').split(',')))
    product_list = Product.objects.all()
    category=Category.objects.all()
    tag=Tag.objects.all()
    text = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Optio officiis reiciendis assumenda. Doloremque odit expedita nisi quis dolorum soluta, qui vel? Dignissimos tenetur magnam, dolorum possimus obcaecati delectus maiores dolor.'
    context = {
        'products': product_list,
        'text':     text,
        'category':category,
        'tag':tag
    }
    return render(request, 'product-list.html', context)

class ProductListView(ListView):
    model=Product
    context_object_name='products'
    template_name='product-list.html'
    paginate_by=2

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context["property_values"] = PropertyValue.objects.all()
        context['category'] = Category.objects.all()
        context['tag'] = Tag.objects.all()
        context["cart"] = Cart.objects.filter(status=False).first()
        context["brand"] = Brand.objects.all()
        return context
    


class ProductDetailView(FormMixin, DetailView):
    model=Product
    form_class = ReviewForm
    context_object_name='product'
    template_name='product-detail.html'

    def get_success_url(self):
        return reverse_lazy('product-detail', kwargs={'pk': self.object.pk})
 
    def get_context_data(self, *args , **kwargs):
        context = super().get_context_data()
        print(self.object)
        context["discount"] = Discount.objects.filter(product = self.object).first()
        context["property_values"] = PropertyValue.objects.filter(product = self.object)
        context["reviews"] = Review.objects.filter(product=self.object)
        context["cart"] = Cart.objects.filter(status=False).first()
        context["related_products"] = Product.objects.filter(category = self.object.category).exclude(id=self.object.pk)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if request.user.is_authenticated:
            if form.is_valid():
                form.instance.product = self.object
                form.instance.author = request.user
                form.save()
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        else:
            return redirect(reverse_lazy('login'))
