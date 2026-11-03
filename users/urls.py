from django.urls import path
from django.contrib.auth.views import LoginView, \
    LogoutView  # -27- Импортируем стандартные контроллеры Django для входа и выхода
from users.apps import UsersConfig
from users.views import RegisterView, ProfileView  # -27- Импортировали ProfileView


# -27- Задаем имя пространства имен для приложения users
app_name = UsersConfig.name

urlpatterns = [
    # -27- Маршрут для страницы регистрации
    path('register/', RegisterView.as_view(), name='register'),

    # -27- Маршрут для авторизации (входа) по email и паролю
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),

    # -27- Маршрут для выхода из системы
    path('logout/', LogoutView.as_view(), name='logout'),

    # -27- Маршрут для редактирования профиля пользователя
    path('profile/', ProfileView.as_view(), name='profile'),
]
