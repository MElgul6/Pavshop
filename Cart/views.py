from django.shortcuts import render,redirect
from Cart.forms import Shipping_infoForm
from Cart.forms import Billing_detailsForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import JsonResponse
from Product.models import Product
from Cart.models import CartItem,Cart
import json
import requests
from Cart.api.serializers import CartCreateSerializer,CartSerializer


def updateItem(request):
    return JsonResponse('item was added', safe=False)

def shopping(request):
    return render(request,'shopping-cart.html')


def checkout(request):
    data=requests.get('http://127.0.0.1:8000/api/cart/', data=request.GET) 
    res=data.json() 
    for i in res:
        print('BODY:', i['cart'])
    form1 = Billing_detailsForm()
    form = Shipping_infoForm()
    if request.method == 'POST':
        form1 = Billing_detailsForm(data = request.POST)
        form = Shipping_infoForm(data = request.POST)
        if form1.is_valid():
            form1.instance.author = request.user
            form1.save()
            return redirect(reverse_lazy('homepage'))
        elif form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect(reverse_lazy('homepage'))
    cart=Cart.objects.filter(status=False).first()
    # print('id',cart.id)
    cartitem=CartCreateSerializer(CartItem.objects.filter(cart=cart)[:1], many=True).data
    context = {
        'form1' : form1,
        'form' : form,
        'cartitem':cartitem
    }
   
    return render(request,'checkout.html',context)


# def paymentComplete(request):
# 	body = json.loads(request.body)
# 	print('BODY:', body)
	
# 	Cart.objects.filter(id=).update(status=True)

# 	return JsonResponse('Payment completed!', safe=False)

    