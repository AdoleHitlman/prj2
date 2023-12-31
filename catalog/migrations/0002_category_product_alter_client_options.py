# Generated by Django 4.2.4 on 2023-08-20 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='наименование')),
                ('description', models.CharField(max_length=100, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='наименование')),
                ('description', models.CharField(max_length=100, verbose_name='описание')),
                ('photo', models.ImageField(upload_to='products/', verbose_name='изображение')),
                ('category', models.CharField(max_length=100, verbose_name='категория')),
                ('price', models.IntegerField(verbose_name='цена')),
                ('create_date', models.DateTimeField(verbose_name='дата создания')),
                ('last_edit_date', models.DateTimeField(verbose_name='дата последнего изменения')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'клиент', 'verbose_name_plural': 'клиенты'},
        ),
    ]
