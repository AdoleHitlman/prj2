# Generated by Django 4.2.4 on 2023-09-13 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_alter_version_options_alter_version_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='version',
            options={'verbose_name': 'Версия', 'verbose_name_plural': 'Версии'},
        ),
    ]
