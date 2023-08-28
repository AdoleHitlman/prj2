from django.shortcuts import render

from catalog.models import Client
from catalog.models import Product
import markdown


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
    with open('README.md', 'r') as file:
        readme_content = file.read()
        html_content1 = markdown.markdown(readme_content)
    with open('requrements.txt', 'r') as file:
        requrements_content = file.read()
        html_content2 = markdown.markdown(requrements_content)
    return render(request, 'catalog/index.html', context={"cont1":{'html_content1': html_content1},"cont2":{'html_content2': html_content2}})


def product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'catalog/product.html', {'product': product})
