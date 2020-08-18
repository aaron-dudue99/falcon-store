from django.shortcuts import render
from django.http import JsonResponse
import json

from .models import *


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total': 0, 'shipping':False}
        cartItems = order['get_cart_items']

    context={'cartItems':cartItems}
    return render(request,'store/index.html', context)

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total': 0, 'shipping':False}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    context={'products':products, 'cartItems':cartItems}
    return render(request,'store/store.html',context = context )

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total': 0, 'shipping':False}
        cartItems = order['get_cart_items']


    context={'items':items, 'order':order, 'cartItems': cartItems}
    return render(request,'store/cart.html',context )

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total': 0, 'shipping':False}
        cartItems = order['get_cart_items']

    context={'items':items, 'order':order, 'cartItems':cartItems}
    return render(request,'store/checkout.html',context = context )

def about(request):
    context= {}
    return render(request, 'store/about.html')

def contact(request):
    context = {}
    return render(request, 'store/contact.html')


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action: ', action)
    print('Product Id: ', productId)

    customer = request.user.customer
    product = Product.objects.get(id = productId)
    order,created = Order.objects.get_or_create(customer = customer, complete = False)
    orderitem , created = OrderItem.objects.get_or_create(order = order, product = product)

    if action == 'add':
        orderitem.quantity = (orderitem.quantity + 1)

    elif action == 'remove':
        orderitem.quantity = (orderitem.quantity - 1)

    orderitem.save()

    if orderitem.quantity <= 0:
        orderitem.delete()

    return JsonResponse('item was added', safe=False)


def processOrder(request):
    print('Data:', request.body)

    return JsonResponse('Payment Complete..', safe = False) 
