from django.db import models

# Create your models here.
class Customer(models.Model): # Nombre de la tabla
	name = models.CharField(max_length = 30) # Campo llamado 'name' de tipo texto, con lóngitud máxima de 30
	address = models.CharField(max_length = 50)	
	email = models.EmailField() # Campo llamado email de tipo email	
	phone = models.CharField(max_length = 7, blank = True, null = True) # blank = True validará que el campo puede ser vació en el formulario, null = True, validará qu en la tabla se pueda guardar coo null este campo

class Article(models.Model):
	name = models.CharField(max_length = 30) # Campo llamado 'name' de tipo texto, con lóngitud máxima de 30
	section = models.CharField(max_length = 20)	
	price = models.IntegerField() # Campo llamado 'price' de tipo entero. no hace falta especificar longitud

class Order(models.Model):
	number = models.IntegerField(verbose_name = 'Order number') # 'verbose_name' sirve para indicar el nombre con el que aparecerá este campo en el navegador
	date = models.DateField() # Campo llamado 'date' de tipo fecha	
	state = models.BooleanField() # Campo llamado 'state' de tipo booleano.
