 # Generated by Django 4.2.4 on 2023-08-23 17:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_category_product_alter_client_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0, verbose_name='цена'),
        ),
    ]
