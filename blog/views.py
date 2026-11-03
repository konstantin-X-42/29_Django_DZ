from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import BlogEntry


class BlogEntryListView(ListView):
    """Просмотр списка статей блога (только опубликованные)"""
    model = BlogEntry
    template_name = 'blog/blogentry_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        # Фильтруем статьи: выводим только те, у которых признак публикации True
        return super().get_queryset().filter(is_published=True)


class BlogEntryDetailView(DetailView):
    """Детальный просмотр одной статьи с увеличением просмотров и отправкой email"""
    model = BlogEntry
    template_name = 'blog/blogentry_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        # Получаем сам объект статьи
        obj = super().get_object(queryset)
        # Увеличиваем счетчик просмотров на 1
        obj.views_count += 1
        obj.save()

        # Проверяем: если просмотров стало ровно 100, отправляем письмо автору
        if obj.views_count == 100:
            send_mail(
                subject=f"Поздравляем! Статья '{obj.title}' набрала популярность!",
                message=f"Ваша блоговая запись '{obj.title}' достигла отметки в 100 просмотров.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=True,  # Защита от падения сервера при ошибках почты
            )

        return obj


class BlogEntryCreateView(CreateView):
    """Создание статьи"""
    model = BlogEntry
    fields = ('title', 'content', 'preview', 'is_published')
    template_name = 'blog/blogentry_form.html'
    success_url = reverse_lazy('blog:list')  # После создания возвращаем к списку


class BlogEntryUpdateView(UpdateView):
    """Редактирование статьи"""
    model = BlogEntry
    fields = ('title', 'content', 'preview', 'is_published')
    template_name = 'blog/blogentry_form.html'

    def get_success_url(self):
        # Динамически перенаправляем на страницу отредактированной статьи
        return reverse('blog:detail', kwargs={'pk': self.object.pk})


class BlogEntryDeleteView(DeleteView):
    """Удаление статьи"""
    model = BlogEntry
    template_name = 'blog/blogentry_confirm_delete.html'
    success_url = reverse_lazy('blog:list')  # После удаления возвращаем к списку
