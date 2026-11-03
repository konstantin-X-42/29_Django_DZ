from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # -27- Убираем username из обязательных полей для авторизации
    username = models.CharField(max_length=150, blank=True, null=True)

    # -27- Делаем email уникальным, основным полем для входа и текст ошибки
    email = models.EmailField(
        unique=True,
        verbose_name='Электронная почта',
        error_messages={
            'unique': "Пользователь с такой электронной почтой уже существует."
        }
    )

    # -27- Три дополнительных поля
    avatar = models.ImageField(upload_to='users/avatars/', blank=True, null=True, verbose_name='Аватар')
    phone = models.CharField(max_length=35, blank=True, null=True, verbose_name='Номер телефона')
    country = models.CharField(max_length=100, blank=True, null=True, verbose_name='Страна')

    # -27- Указываем, что для авторизации используется email вместо username
    USERNAME_FIELD = 'email'

    # -27- Список дополнительных обязательных полей оставляем пустым
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
