from django.shortcuts import get_object_or_404, render
from category.models import Category
from .models import Product
# Create your views here.

def store(request, category_slug=None):
    categories = None
    products = None
    if category_slug !=None:
        categories=get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(Category=categories, is_available=True)
        products_count = products.count()
    else: 
        products = Product.objects.all().filter(is_available=True)
        products_count = products.count()
    context = {'products': products, 'count':products_count}
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):

    single_product = Product.objects.get(Category__slug=category_slug, slug=product_slug)
    
    context = {'single_product': single_product}
    return render(request, 'store/product_detail.html', context)