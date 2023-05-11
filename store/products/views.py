from django.shortcuts import render, HttpResponse
from products.models import ProductCategory, Product

def index(request): 
    context = {
        'title' : 'Test title',
        'is_promotion': True, 
    } 
    return render(request, 'index.html', context)

def products(request):
    context = {
        'title' : 'Store - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()
    } 
    return render(request, 'products.html', context)

 
