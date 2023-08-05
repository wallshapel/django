from django.http import HttpResponse
from django.shortcuts import render # Ayuda a simplificar la forma de renderizar plantillas
import datetime

def greet(request):	
	now = datetime.datetime.now()
	subjects = ['templates', 'models', 'forms']
	return render(request, 'index.html', {'name': 'Legato', 'now': now, 'subjects': subjects}) # A través de un diccionario como este podemos pasar información al template. Es obligatorio pasar el request

def son(request):
	return render(request, 'son.html')