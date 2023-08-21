from django.core.management.base import BaseCommand
from catalog.models import Category

class Command(BaseCommand):
    help = 'Очищает бд и наполняет новыми данными'

    def handle(self, *args, **options):
        # Delete all existing data from the Category model
        Category.objects.all().delete()

        # Create new Category objects and save them to the database
        categories = ['программы', 'игры', 'прочее']
        for category_name in categories:
            category = Category(name=category_name)
            category.save()

        self.stdout.write(self.style.SUCCESS('Выполнено,База данных наполненна новыми данными'))