from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart(object):
    def __init__(self, request):
        # cart is initialized with a request object
        # current session is stored by:
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # create an empty cart
            cart = self.session[settings.CART_SESSION_ID] = {} 
        self.cart = cart 
    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity 
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()
    def save(self):
        self.session.modified = True 