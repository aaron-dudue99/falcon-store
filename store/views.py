from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    context={}
    return render(request,'store/index.html', context)

def store(request):
    products = Product.objects.all()
    context={'products':products}
    return render(request,'store/store.html',context = context )

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()

    else:
        items = []


    context={'items':items}
    return render(request,'store/cart.html',context )

def checkout(request):
    context={}
    return render(request,'store/checkout.html',context = context )

def about(request):
    context= {}
    return render(request, 'store/about.html')

def contact(request):
    context = {}
    return render(request, 'store/contact.html')


