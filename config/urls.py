from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),

                  # -22- Подключение маршрутов приложения catalog
                  path('', include('catalog.urls', namespace='catalog')),

                  # -25- Подключение маршрутов приложения блога (все адреса будут начинаться с blogs/)
                  path('blogs/', include('blog.urls', namespace='blog')),

                  # -27- Подключение маршрутов приложения пользователей (все адреса будут начинаться с users/)
                  path('users/', include('users.urls', namespace='users')),
              ] + static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)  # -23- правильная обработка статических файлов
