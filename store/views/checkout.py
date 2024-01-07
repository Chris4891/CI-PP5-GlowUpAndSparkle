import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from store.views.cart import Cart
from store.models.orders import Products  # Import the Cart model



stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(request):
    # Retrieve cart items from the session
    cart = request.session.get('cart', {})
    line_items = []

    for product_id, quantity in cart.items():
        # Retrieve the product details from your database
        product = Products.objects.get(id=product_id)

        # Create a line item for the Stripe session
        line_item = {
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': product.name,
                    
                },
                'unit_amount': int(product.price * 100),  # Convert price to cents
            },
            'quantity': quantity,
        }

        line_items.append(line_item)

    # Create a new Checkout Session with the line items
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=request.build_absolute_uri(reverse('orderdetails')),
        cancel_url=request.build_absolute_uri(reverse('cancel')),
    )

    return redirect(session.url)


def success(request):
    return render(request, 'success.html')

def cancel(request):
    return render(request, 'cancel.html')

from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Products
from store.models.orders import Order
from django.shortcuts import get_object_or_404

from django.core.mail import send_mail


def orderdetails(request):
    error_message = None  
    if request.method == 'POST':
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer_id = request.session.get('customer')
        customer = get_object_or_404(Customer, id=customer_id)
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))
        print(address, phone, customer_id, cart, products)


        if not (address and phone ):
            print("Form data is missing")
            error_message = "All fields are required."
            return render(request, 'orderdetails.html', {'error_message': error_message})

        
        if len (phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
            return render(request, 'orderdetails.html', {'error_message': error_message})

        else:
            for product in products:
                    print(cart.get(str(product.id)))
                    order = Order(
                                    customer=customer,
                                    product=product,
                                    price=product.price,
                                    address=address,
                                    phone=phone,
                                    quantity=cart.get(str(product.id)))
                    order.save()
            context = {'email': customer.email}
            email_content = "Thank You For Trusting Us And Order <br> Your order will arive Soom!"

            email_subject = 'Order Placed'
            recipient_list = [customer.email]
            from_email = 'shahwaizali189@gmail.com'

            send_mail(
                email_subject,
                '',
                from_email,
                recipient_list,
                html_message=email_content,
                fail_silently=False
            )

            owner_email = "shahwaizmughal02@gmail.com"
            send_mail(
                "New Order Placed",
                f"New order placed with details: {customer.first_name},{customer.last_name},\n,{address}, {phone}, {products}",  
                from_email,
                recipient_list=[owner_email],
                fail_silently=False
            )

            request.session['cart'] = {}
        return render(request, 'success.html', {'error_message': error_message})
    else:
        return render(request, 'orderdetails.html', {'error_message': error_message})





