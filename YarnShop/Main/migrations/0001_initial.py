# Generated by Django 4.2.5 on 2023-11-12 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(db_index=True, max_length=50, verbose_name='Категория товара')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Tovar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_tovar', models.CharField(max_length=128, verbose_name='Название товара')),
                ('price_tovar', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость товара')),
                ('img_tovar', models.ImageField(blank=True, upload_to='')),
                ('url_tovar', models.URLField(blank=True, max_length=300)),
                ('description', models.TextField(blank=True, verbose_name='Описание товара')),
                ('slug', models.CharField(db_index=True, max_length=150, unique=True)),
                ('stock', models.PositiveIntegerField()),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category_tovar', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='tovars', to='Main.category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ('name_tovar',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
