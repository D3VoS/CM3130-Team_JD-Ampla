from django.contrib import admin
from django.urls import path, include
from . import views
app_name = "Store"
urlpatterns = [
    path('', views.index, name='store_index'),
    path('addProduct', views.AddProduct, name='add_product'),
    path('removeProduct/<int:id>', views.RemoveProduct, name='remove_product')
]
