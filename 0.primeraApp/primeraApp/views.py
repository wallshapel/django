from django.http import HttpResponse
import datetime

def greet(request): # Primera vista
	return HttpResponse('Hello World from Django!')

def farewell(request):
	return HttpResponse('Goodbye!')

def get_time(request):
	return HttpResponse(datetime.datetime.now()) # Devuelve la fecha en formato yyyy-MM-dd hh:mm:ss.mmm 

def calculate_age(request, age, ano):
	current_year = int(datetime.datetime.strftime(datetime.datetime.now(), '%Y'))
	return HttpResponse(age + (ano - current_year))
