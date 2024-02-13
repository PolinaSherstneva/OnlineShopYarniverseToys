
from django.urls import path
from . import views
from users import views as user_views


urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('lk', views.lk, name="lk"),
    path('catalog', views.catalog, name="catalog"),
    path('create', views.create, name="create"),
    path('Tovar/<int:pk>', views.TovarDetailView.as_view(), name='tovar-detail'),
    path('<int:pk>/update', views.TovarUpdateView.as_view(), name='tovar-update'),
    path('<int:pk>/delete', views.TovarDeleteView.as_view(), name='tovar-delete'),
]
