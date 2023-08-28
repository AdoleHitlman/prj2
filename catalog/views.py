from django.shortcuts import render

from catalog.models import Client
from catalog.models import Product


# Create your views here.

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name},{phone},{message}')
        Client.objects.create(name=name, phone=phone, message=message)
    return render(request, 'catalog/contacts.html')


def catalog(request):
    products = Product.objects.all()
    return render(request, 'catalog/catalog.html', context={'products': products})


def menu(request):
    return render(request, 'catalog/menu.html')


def index(request):
    return render(request, 'catalog/index.html')


def product(request, product_id):
    products = Product.objects.get(id=product_id)
    return render(request, 'catalog/product.html', {'product': product})
