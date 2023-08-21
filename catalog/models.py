from django.db import models
from django.utils import timezone


# Create your models here.
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


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.CharField(max_length=100, verbose_name='описание')
    photo = models.ImageField(upload_to='products/', verbose_name="изображение")
    category = models.CharField(max_length=100, verbose_name='категория')
    price = models.IntegerField(default=0,verbose_name="цена")
    create_date = models.DateTimeField(default=timezone.now, verbose_name="дата создания")
    last_edit_date = models.DateTimeField(verbose_name="дата последнего изменения")

    def __str__(self):
        return f"{self.pk},{self.name},{self.price},{self.category}"

    class Meta:
        verbose_name = 'продукт'  # Настройка для наименования одного объекта
        verbose_name_plural = 'продукты'  # Настройка для наименования набора объектов


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=100, verbose_name='описание')

    def __str__(self):
        return f"{self.pk},{self.description}"

    class Meta:
        verbose_name = 'категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'  # Настройка для наименования набора объектов
