from .models import Tovar
from django.forms import ModelForm, TextInput, Textarea,  Select


class TovarForm(ModelForm):
    class Meta:
        model = Tovar
        fields = ['name_tovar', 'price_tovar', 'category_tovar', 'slug', 'url_tovar', 'description', 'stock', 'img_tovar']

        widgets = {
            "name_tovar": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название товара'
            }),
            "category_tovar": Select(attrs={
                'class': 'form-control',
                'select': 'Категория товара'
            }),

            "url_tovar": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'URL товара'
            }),

            "price_tovar": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Стоимость товара'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание товара'
            }),
            "stock": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Остатки товара'
            }),
            "slug": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Slug товара'
            }),


        }
