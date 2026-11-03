import os
from django import forms
from django.core.exceptions import ValidationError
from catalog.models import Product

# -26-Задание 1: Список запрещенных слов
FORBIDDEN_WORDS = [
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
]


class ProductForm(forms.ModelForm):
    """ -24- Класс Form отвечает за генерацию HTML-полей на странице, сбор данных от пользователя и их базовое оформление."""
    class Meta:
        model = Product
        # -24- Поля модели для заполнения пользователем
        fields = ['name', 'description', 'image', 'category', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # -24- Сохраняем красивую стилизацию для всех полей
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'style': 'width: 100%; padding: 10px; margin-bottom: 15px; border: 1px solid #dee2e6; border-radius: 6px; box-sizing: border-box; font-size: 1rem;'
            })

    # -26-Задание 1: Валидация наименования (в любом регистре)
    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        name_lower = name.lower()
        for word in FORBIDDEN_WORDS:
            if word in name_lower:
                raise ValidationError(f"Наименование не может содержать запрещенное слово '{word}'.")
        return name

    # -26-Задание 1: Валидация описания (в любом регистре)
    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        if description:  # -26- Проверяем, так как поле может быть пустым (blank=True)
            description_lower = description.lower()
            for word in FORBIDDEN_WORDS:
                if word in description_lower:
                    raise ValidationError(f"Описание не может содержать запрещенное слово '{word}'.")
        return description

    # -26-Задание 2: Кастомная валидация цены через метод clean_price
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise ValidationError("Цена продукта не может быть отрицательной.")
        return price

    # -26-Дополнительное задание*: Валидация формата и размера изображения
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # -26- Проверка размера (5 МБ = 5 * 1024 * 1024 байт)
            max_size = 5 * 1024 * 1024
            if image.size > max_size:
                raise ValidationError("Размер файла не должен превышать 5 МБ.")

            # -26- Проверка расширения файла
            ext = os.path.splitext(image.name)[1].lower()
            valid_extensions = ['.jpg', '.jpeg', '.png']
            if ext not in valid_extensions:
                raise ValidationError("Допускаются только файлы форматов JPEG или PNG.")
        return image


# -28- Специальная форма для модераторов, позволяющая только менять статус публикации
class ProductModeratorForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['is_published']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # -28- Применяем стилизацию для поля модератора
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'style': 'margin-bottom: 15px; transform: scale(1.2); margin-left: 10px;'
            })
