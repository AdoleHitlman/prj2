# Generated by Django 4.2.4 on 2023-08-20 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='имя')),
                ('phone', models.CharField(max_length=20, verbose_name='телефон')),
                ('message', models.CharField(max_length=500, verbose_name='сообщение')),
            ],
            options={
                'verbose_name': 'покупатель',
                'verbose_name_plural': 'покупатели',
            },
        ),
    ]
