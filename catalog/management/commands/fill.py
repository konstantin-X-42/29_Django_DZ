from django.core.management import call_command
from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Очищает базу данных и загружает тестовые данные из фикстур'

    def handle(self, *args, **options):
        # 1. Сначала удаляем старые данные
        self.stdout.write(self.style.WARNING('Очистка старых данных'))
        Product.objects.all().delete()
        Category.objects.all().delete()

        # 2. Загружаем данные из файла фикстур
        self.stdout.write(self.style.MIGRATE_LABEL('Загрузка новых данных из фикстур'))
        try:
            # Вызываем loaddata для файла 23_catalog.json
            call_command('loaddata', '23_catalog.json')

            self.stdout.write(self.style.SUCCESS('База данных успешно очищена и наполнена из 23_catalog.json'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при загрузке фикстур: {e}'))
