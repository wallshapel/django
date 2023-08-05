from django.contrib import admin
from django.urls import path

from gestion_pedidos.views import products, find

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', products, name = 'products'),
    path('find/', find, name = 'find')
]
