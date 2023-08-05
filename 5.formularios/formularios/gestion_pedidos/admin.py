from django.contrib import admin
from gestion_pedidos.models import Customer, Article, Order # Importamos el modelo 'Customer'
# Register your models here.

class CustumerAdmin(admin.ModelAdmin):
	list_display = ('name', 'address', 'email', 'phone') # Con esto mostramos los campos que queremos mostrar, pudiendo no motrarlos todos, como contraseñas por ejemplo
	search_fields = ('name', 'address', 'email', 'phone') # Con esto podemos agregar un campo de búsqueda en la vista que busque por los campos que hemos especiicado

admin.site.register(Customer, CustumerAdmin) # Esto hará que en el panel de administración aparezca en una sección, el apartado de gestion de pedidos y el modelo Customers, con la opción de agregar y modificar y posteriormente eliminar sus respectivos registros

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('name', 'section', 'price')
	search_fields = ('name', 'section', 'price')
	list_filter = ('section',) # Con esto agregamos un apartado en el panel de adminstración en el que podemos filtrar los artículos por sección. Importante la , al final si solo vamos a incluir un solo elmento a la tupla.

admin.site.register(Article, ArticleAdmin) 

class OrderAdmin(admin.ModelAdmin):
	list_display = ('number', 'date', 'state')
	search_fields = ('number', 'date', 'state')
	list_filter = ('date',)
	date_hierarchy = 'date' # Con esto logramos que aparescan una especie de pestañas que serviran para filtrar los registros de una manera pro 

admin.site.register(Order, OrderAdmin)
