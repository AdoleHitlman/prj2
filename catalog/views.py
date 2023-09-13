import markdown
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, ListView, UpdateView

from catalog.forms import BlogForm
from catalog.forms import ProductForm
from catalog.models import Blog
from catalog.models import Client
from catalog.models import Product
from catalog.models import Version


# Create your views here.
class CreateProductView(View):

    def get(self, request):
        form = ProductForm()
        return render(request, 'create_product.html', {'form': form})

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        return render(request, 'create_product.html', {'form': form})


class ContactsView(View):
    @staticmethod
    def post(request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name},{phone},{message}')
        Client.objects.create(name=name, phone=phone, message=message)
        return render(request, 'catalog/contacts.html')

    @staticmethod
    def get(request):
        return render(request, 'catalog/contacts.html')


class CatalogView(View):
    def get(self, request):
        products = Product.objects.all()
        active_versions = Version.objects.filter(is_current_version=True)
        return render(request, 'catalog.html', {'products': products, 'active_versions': active_versions})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog')
        products = Product.objects.all()
        return render(request, 'catalog.html', {'products': products, 'form': form})


class IndexView(View):
    @staticmethod
    def get(request):
        with open('README.md', 'r') as file:
            readme_content = file.read()
            html_content1 = markdown.markdown(readme_content)
        with open('requrements.txt', 'r') as file:
            requrements_content = file.read()
            html_content2 = markdown.markdown(requrements_content)
        blogs = Blog.objects.all()
        form = BlogForm()
        return render(request, 'catalog/index.html',
                      context={"cont1": {'html_content1': html_content1}, "cont2": {'html_content2': html_content2},
                               "cont3": {'blogs': blogs}})

    def post(self, request):
        form = BlogForm(request.POST, request.FILES)  # Инициализация формы с данными запроса и файлами
        if form.is_valid():
            form.save()  # Сохранение статьи
            return redirect('/')  # Перенаправление обратно на главную страницу
        else:
            blogs = Blog.objects.all()
            return render(request, 'catalog/index.html', {'blogs': blogs, 'form': form})


class ProductView(View):
    @staticmethod
    def get(request, product_id):
        product = Product.objects.get(id=product_id)
        return render(request, 'catalog/product.html', {'product': product})


class BlogDetailView(DetailView):
    model = Blog

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Увеличиваем счетчик просмотров
        self.object.views_count += 1
        self.object.save()
        return super().get(request, *args, **kwargs)


class PublishedBlogListView(ListView):
    model = Blog

    def get_queryset(self):
        # Фильтруем только опубликованные записи
        return super().get_queryset().filter(is_published=True)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'preview']
    template_name = 'blog_update.html'

    def get_success_url(self):
        # Получаем URL страницы просмотра отредактированной статьи
        return reverse('blog-detail', kwargs={'pk': self.object.pk})
