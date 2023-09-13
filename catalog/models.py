from django.db import models
from django.utils import timezone
from slugify import slugify


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.CharField(max_length=100, verbose_name='описание')
    photo = models.ImageField(upload_to='products/', verbose_name="изображение")
    category = models.CharField(max_length=100, verbose_name='категория')
    price = models.IntegerField(default=0, verbose_name="цена")
    create_date = models.DateTimeField(default=timezone.now, verbose_name="дата создания")
    last_edit_date = models.DateTimeField(default=timezone.now, verbose_name="дата последнего изменения")

    def __str__(self):
        return f"{self.pk},{self.name},{self.price},{self.category}"

    def get_active_version(self):
        return self.versions.filter(is_current_version=True).first()

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='versions')
    version_number = models.CharField(max_length=50, verbose_name="Номер версии")
    version_name = models.CharField(max_length=100, verbose_name="Название версии")
    is_current_version = models.BooleanField(default=False, verbose_name="Текущая версия")

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя')
    phone = models.CharField(max_length=20, verbose_name='телефон')
    message = models.CharField(max_length=500, verbose_name='сообщение')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} {self.phone} {self.name}'

    class Meta:
        verbose_name = 'клиент'  # Настройка для наименования одного объекта
        verbose_name_plural = 'клиенты'  # Настройка для наименования набора объектов


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=100, verbose_name='описание')

    def __str__(self):
        return f"{self.pk},{self.description}"

    class Meta:
        verbose_name = 'категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'  # Настройка для наименования набора объектов


class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True, blank=True)
    content = models.TextField()
    preview = models.ImageField(upload_to='previews/')
    created_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.pk},{self.title}'

    def save(self, *args, **kwargs):
        # Автоматически генерируем slug из заголовка перед сохранением записи
        self.slug = slugify(str(self.title))
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Статья'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Статьи'  # Настройка для наименования набора объектов
