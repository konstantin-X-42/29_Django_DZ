from django.db import models


class BlogEntry(models.Model):
    title = models.CharField(max_length=250, verbose_name="Заголовок")
    slug = models.CharField(
        max_length=250, verbose_name="slug", blank=True, null=True
    )
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(
        upload_to="blog_previews/",
        verbose_name="Превью (изображение)",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )
    is_published = models.BooleanField(
        default=True, verbose_name="Признак публикации"
    )
    views_count = models.PositiveIntegerField(
        default=0, verbose_name="Количество просмотров"
    )

    class Meta:
        verbose_name = "Блоговая запись"
        verbose_name_plural = "Блоговые записи"

    def __str__(self):
        return self.title
