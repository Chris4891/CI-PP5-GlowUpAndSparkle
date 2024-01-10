from django.contrib import admin
from django.urls import path
from .views.home import Index 
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
# from .views.checkout import checkout
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware
from .views.store import store
from .views.contact import  contact_page,response
from .views.about import About
from .views.ppolicy import ppolicy
from .views.checkout import create_checkout_session, success, cancel,orderdetails
from .views.newsletter import Newsletter
from .views.productdetail import ProductDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Index.as_view(), name='homepage'),

    path('store/', store.as_view() , name='store'),
    path('contact/', contact_page , name='contact_page'),
    # path('', subscribe , name='subscribe'),
    path('about/', About.as_view() , name='about'),
    path('response/', response.as_view() , name='response'),

    path('privacypolicy/', ppolicy.as_view() , name='privacypolicy'),
    path('orderdetails/', orderdetails , name='orderdetails'),

    path('orderdetails-guest/', orderdetails_guest, name='orderdetails_guest'),

    path('signup', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('checkout/', create_checkout_session, name='create_checkout_session'),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel'),

    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('cart/', auth_middleware(Cart.as_view()) , name='cart'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='productdetails'),
    path('subscribe/', Newsletter, name='newsletter'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

