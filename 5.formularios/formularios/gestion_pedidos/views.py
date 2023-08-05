from django.http import HttpResponse
from django.shortcuts import render
from gestion_pedidos.models import Article

# Create your views here.
def products(request):
	return render(request, 'products.html')

def find(request):
	return HttpResponse('Search item: %r' %request.GET['product'])
