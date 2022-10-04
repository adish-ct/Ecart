from django.shortcuts import render, redirect, get_object_or_404
from ecart_app.models import Product
from cart_app.models import Cart, Cart_Item
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

# view 1 create a session for store datas temporarily

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


# view 2 add products to cart

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()
    try:
        cart_item = Cart_Item.objects.get(product=product, cart=cart)

        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
            cart_item.save()
    except Cart_Item.DoesNotExist:
        cart_item = Cart_Item.objects.create(product=product, quantity=1, cart=cart)
        cart.save()
    return redirect('cart_app:cart_details')


# view 3 cart details

def cart_details(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = Cart_Item.objects.filter(cart=cart, active=True)
        for item in cart_items:
            total += (item.product.price * item.quantity)
            counter += item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter))

# view 4 cart items remove

def cart_remove(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = Cart_Item.objects.get(product=product, cart=cart)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_app:cart_details')

# view 5 cart items delete

def cart_delete(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = Cart_Item.objects.get(product=product, cart=cart)
    cart_item.delete()

    return redirect('cart_app:cart_details')