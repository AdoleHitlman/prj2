from django.shortcuts import render
from catalog.models import Client
from .models import Product
# Create your views here.

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name},{phone},{message}')
        Client.objects.create(name=name,phone=phone,message=message)
    return render(request, 'catalog/contacts.html')

def catalog(request):
    return render(request, 'catalog/catalog.html')

def menu(request):
    return render(request, 'catalog/menu.html')

def base(request):
    return render(request, 'catalog/base.html')


def products(request):
    products = Product.objects.all()  # здесь Product - ваша модель продукта
    return render(request, 'product.html', {'products': products})