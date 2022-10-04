from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.

# view 1

def all_product_category(request, c_slug=None):
    category_page = None
    product_list = None
    if c_slug != None:
        category_page = get_object_or_404(Category, slug=c_slug)
        product_list = Product.objects.all().filter(category=category_page, available=True)

    else:
        product_list = Product.objects.all().filter(available=True)

    paginator = Paginator(product_list, 6)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, 'category.html', {'category': category_page, 'products': products})


def product_detail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'detail_page.html', {'product': product})
