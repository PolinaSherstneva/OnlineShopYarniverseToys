from django.db import models


class Category(models.Model):
    name_category = models.CharField(max_length=50, verbose_name="Категория товара", db_index=True)

    def __str__(self):
        return self.name_category

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Tovar(models.Model):
    name_tovar = models.CharField(max_length=128, verbose_name="Название товара")
    category_tovar = models.ForeignKey(Category, related_name='tovars', on_delete=models.CASCADE, blank=True, default='')
    price_tovar = models.DecimalField(max_digits=10, verbose_name="Стоимость товара", decimal_places=2)
    img_tovar = models.ImageField(upload_to='', blank=True)
    url_tovar = models.URLField(max_length=300, blank=True)
    description = models.TextField(verbose_name="Описание товара", blank=True)
    slug = models.CharField(max_length=150, db_index=True, unique=True)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_tovar

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ('name_tovar',)
        index_together = (('id', 'slug'),)

