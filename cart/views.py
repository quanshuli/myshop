from django.shortcuts import render, redirect, get_list_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm

#only allow POST request
@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_list_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})

    