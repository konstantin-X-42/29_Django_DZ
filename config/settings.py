import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# Загружаем переменные из файла .env
load_dotenv(BASE_DIR / '.env')

SECRET_KEY = os.getenv('SECRET_KEY') # импорт из .env

DEBUG = True if os.getenv('DEBUG') == 'True' else False  # импорт из .env

ALLOWED_HOSTS = ['*']  # ['*'] - Django-сайт разрешено открывать по любому сетевому адресу (хосту) или домену.


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalog',  # добавляем приложение
    'blog',
    'users',    # -27- Подключаем новое созданное приложение для работы с пользователями
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'config.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'config.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # БЗ PostgresSQL
        'NAME': os.getenv('NAME'),                  # импорт из .env
        'USER': os.getenv('USER'),                  # импорт из .env
        'PASSWORD': os.getenv('PASSWORD'),          # импорт из .env
        'HOST': os.getenv('HOST'),                  # импорт из .env
        'PORT': os.getenv('PORT'),                  # импорт из .env
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# -27- Меняем основной язык проекта на русский (вывод системных предложений)
LANGUAGE_CODE = 'ru'

# -27- Выставляем московское время (или оставить UTC)
TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]


MAILERS = {
    'default': {
        'BACKEND': 'django.core.mail.backends.console.EmailBackend',
    },
}

# Django-проект, физически хранит загруженные пользователями файлы (картинки, документы)
# и по какому интернет-адресу к ним обращаться.
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# -25- Стандартные настройки почты Django для задания со звездочкой
DEFAULT_FROM_EMAIL = 'webmaster@localhost'
ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')  # Безопасный импорт из .env email для отправки поздравления

# -27- Указываем Django использовать нашу кастомную модель User из приложения users вместо стандартной
AUTH_USER_MODEL = 'users.User'

# -27- Указываем имя маршрута, по которому Django найдёт твой шаблон home.html
LOGIN_REDIRECT_URL = 'catalog:21-2_home1'

# -27- То же самое для перенаправления после выхода из системы
LOGOUT_REDIRECT_URL = 'catalog:21-2_home1'
