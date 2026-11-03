from django.urls import path
from catalog.views import (
    ProductListView,        # -25- Импорт контроллера главной страницы, вывод списка всех товаров из базы данных
    CategoriesListView,     # -25- Импорт контроллера отображения списка объектов
    OrdersTemplateView,     # -25- Импорт контроллера отобразить HTML-страницу заказов без сложной логики
    ContactsTemplateView,   # -25- Импорт контроллера отображения статической или полустатической страницы (контактов)
    ProductDetailView,      # -25- Импорт контроллера отображение детальной информации об одном конкретном объекте
    ProductCreateView,      # -25- Импорт контроллера создания новой записи в базе данных через HTML-форму
    ProductUpdateView,      # -26- Импорт контроллера обновления
    ProductDeleteView,      # -26- Импорт контроллера удаления
    ProductManageListView,  # -26- Импорт контроллера вывода всех товаров в панель управления
)

# исключаем одноименные конфликты
app_name = 'catalog'

urlpatterns = [
    # -22- маршрут URL, для домашней страницы 1
    path('', ProductListView.as_view(), name='21-2_home1'),

    # -22- маршрут URL, для Категорий страница 2
    path('categories/', CategoriesListView.as_view(), name='21-2_home2'),

    # -22- маршрут URL, для Заказов страница 3
    path('orders/', OrdersTemplateView.as_view(), name='21-2_home3'),

    # -22- маршрут URL, для страницы 4 контактов с закрывающим /
    path('contacts/', ContactsTemplateView.as_view(), name='21-2_home4'),

    # -24-Задание 1 Маршрут URL, отвечает за динамическое отображение страницы конкретного товара
    # (например, карточки товара с его подробным описанием, ценой и картинкой).
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

    # -24-Задание 1 Маршрут URL, для создания товара
    path('products/create/', ProductCreateView.as_view(), name='create_product'),

    # -26- Маршрут URL, для редактирования товара
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='update_product'),

    # -26- Маршрут URL, для удаления товара
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_product'),

    # -26- Маршрут URL, для отображения страницы панели управления товарами
    path('products/manage/', ProductManageListView.as_view(), name='manage_products'),

]
