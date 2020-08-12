from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return render(request,'store/index.html',context = context )

def store(request):
    context={}
    return render(request,'store/store.html',context = context )

def cart(request):
    context={}
    return render(request,'store/cart.html',context = context )

def checkout(request):
    context={}
    return render(request,'store/checkout.html',context = context )

def about(request):
    context= {}
    return render(request, 'store/about.html')

def contact(request):
    context = {}
    return render(request, 'store/contact.html')


