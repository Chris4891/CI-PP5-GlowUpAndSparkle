from django.shortcuts import render , redirect
from django.http import HttpResponse
from store.models.product import Products
from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import Products
from django.contrib import messages


class Cart(View):
    def get(self, request):
        cart = request.session.get('cart', {})  # Use get with a default value to avoid None
        if cart:
            ids = list(cart.keys())
            products = Products.get_products_by_id(ids)
            print(products)
        else:
            products = []  # Define an empty list when the cart is empty

        return render(request, 'cart.html', {'products': products})
    
    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])

        return redirect('cart')
