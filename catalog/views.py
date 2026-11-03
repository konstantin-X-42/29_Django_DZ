from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # -28- Импорт миксины для проверки прав доступа
from django.http import Http404 # -28- Импорт исключения для запрета доступа
from catalog.models import Product, ContactInfo, Category
from catalog.forms import (ProductForm,
                           ProductModeratorForm) # -28- Импорт формы views.py

class ProductListView(ListView):
    """-25- Контроллер главной страницы"""
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

    def get_queryset(self):
        # -25- Получаем базовый набор товаров
        queryset = super().get_queryset()

        # -28- Если пользователь модератор или суперпользователь — показываем все товары
        if self.request.user.has_perm('catalog.can_unpublish_product'):
            return queryset

        # -28- Для обычных пользователей и гостей выводим только опубликованные товары
        return queryset.filter(is_published=True)



class CategoriesListView(ListView):
    """-25- Контроллер для страницы категорий"""
    model = Category # -26- Исправил модель
    template_name = 'catalog/21-2_home2.html'
    context_object_name = 'categories' # -26- Исправил имя контекста



class OrdersTemplateView(TemplateView):
    """-25- Контроллер для страницы заказов"""
    template_name = 'catalog/21-2_home3.html'



class ContactsTemplateView(TemplateView):
    """-25- Контроллер страницы контактов"""
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # -25- Получаем данные контактов
        try:
            context['contact_data'] = ContactInfo.objects.first()
        except Exception:
            context['contact_data'] = None
        return context

    def post(self, request, *args, **kwargs):
        # -25- Обработка отправки формы обратной связи
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(f"Новое сообщение!")
        print(f"Имя: {name} | Email: {email}")
        print(f"Текст: {message}")
        print("-" * 20)

        # -25- Рендерим страницу обратно с сообщением успешно
        context = self.get_context_data()
        context['success_message'] = 'Спасибо! Ваше сообщение успешно отправлено.'
        return self.render_to_response(context)



class ProductDetailView(DetailView):
    """-25- Контроллер страницы с подробной информацией о товаре"""
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'



class ProductCreateView(LoginRequiredMixin, CreateView):
    """-25- Контроллер формы для создания нового товара с защитой и валидацией"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:21-2_home1')  # -25- Перенаправление на главную после создания

    # -28- При создании продукта автоматически сохраняем авторизованного пользователя в поле owner
    def form_valid(self, form):
        product = form.save(commit=False)
        product.owner = self.request.user
        product.save()
        return super().form_valid(form)


# -26- ProductUpdateView и ProductDeleteView контроллеры для полного CRUD

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """-26- Контроллер для редактирования существующего товара с динамическим разделением прав"""
    model = Product
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:21-2_home1')

    # -28- Если пользователь владелец (или поле owner пустое, но пользователь его создал) — даем полную форму
    def get_form_class(self):
        product = self.get_object()

        # -28- Приоритет владельцу: если товар принадлежит пользователю, даем редактировать всё
        if product.owner == self.request.user:
            return ProductForm

        # -28- Если пользователь модератор и товар ЧУЖОЙ — даем только чекбокс публикации
        if self.request.user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm

        return ProductForm

    # -28- Проверяем право на вход: пускаем если владелец ИЛИ если есть права модератора
    def test_func(self):
        product = self.get_object()
        is_owner = product.owner == self.request.user
        is_moderator = self.request.user.has_perm('catalog.can_unpublish_product')
        return is_owner or is_moderator

    def handle_no_permission(self):
        raise Http404("У вас нет прав для изменения этого продукта.")



class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """-26- Контроллер для удаления товара"""
    model = Product
    template_name = 'catalog/product_confirm_delete.html'  # -26- Нужен будет шаблон подтверждения
    success_url = reverse_lazy('catalog:21-2_home1')  # -26- Перенаправление на главную после удаления

    # -28- Удалить продукт может либо его создатель (owner), либо модератор с правом удаления любого продукта
    def test_func(self):
        product = self.get_object()
        is_owner = self.request.user == product.owner
        is_moderator = self.request.user.has_perm('catalog.delete_product')
        return is_owner or is_moderator

    # -28- Если проверку не прошёл — возвращаем ошибку 403 / 404
    def handle_no_permission(self):
        raise Http404("У вас нет прав на удаление этого продукта.")



class ProductManageListView(ListView):
    """-26- Контроллер страницы управления товарами (изменение/удаление)"""
    model = Product
    template_name = 'catalog/product_manage.html'
    context_object_name = 'products'
