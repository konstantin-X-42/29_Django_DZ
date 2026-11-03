from django.db import models
from django.conf import settings # -28- импортируем настройки для получения связи с кастомной моделью пользователя

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    # -28- Поле добавлено, тип BooleanField, default=False указывает на статус «не опубликован»
    is_published = models.BooleanField(default=False, verbose_name='Опубликован')

    # -28- Связываем продукт с моделью пользователя через ForeignKey. При удалении пользователя продукты остаются (owner=null)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name='Владелец',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        # -28- Добавляем кастомные права к модели продукта для роли «Модератор продуктов»
        permissions = [
            ("can_unpublish_product", "Может отменять публикацию продукта"),
        ]


class ContactInfo(models.Model):
    """Класс хранения контактных данных"""
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')
    address = models.TextField(verbose_name='Адрес')

    def __str__(self):
        return "Контактная информация компании"

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'
