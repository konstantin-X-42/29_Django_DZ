# -29- Подключаем встроенные механизмы низкоуровневого кэширования Django (Задание 4)
from django.core.cache import cache
from django.conf import settings
from catalog.models import Product


def get_products_by_category(category_id):
    """
    # -29- Сервисная функция возвращает список продуктов по ID категории (Задание 3)
    # -29- Реализует низкоуровневое кэширование по ключу category_{id} (Задание 4)
    """
    # -29- Формируем ключ по шаблону category_{id} строго согласно ТЗ (Задание 4)
    cache_key = f"category_{category_id}"

    # -29- Пытаемся получить данные из оперативной памяти Redis (Задание 4)
    products = cache.get(cache_key)

    # -29- Проверяем, если кэш пуст, то идем делать "тяжелый" запрос в БД (Задание 4)
    if products is None:
        # -29- Получаем список объектов из БД и преобразуем в list для кэширования
        products = list(Product.objects.filter(category_id=category_id, is_published=True))

        # -29- Записываем данные в Redis с TTL, заданным в файле конфигурации settings.py (Задание 4)
        cache.set(cache_key, products, timeout=settings.CACHE_TTL)

    return products
