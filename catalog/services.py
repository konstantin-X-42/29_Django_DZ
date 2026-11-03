# -29- Файл сервисного слоя для изоляции работы с данными категорий (Задание 3)
from catalog.models import Product

def get_products_by_category(category_id):
    """ -29- Сервисная функция, возвращает список всех продуктов в указанной категории (Задание 3)"""
    # -29- Делаем запрос к базе данных, отфильтровав только опубликованные товары для выбранной категории
    products = list(Product.objects.filter(category_id=category_id, is_published=True))
    return products
