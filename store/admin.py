from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.contact import ContactMessage
from store.models.newsletter import Subscriber

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'category','price', 'description']
    list_filter = ('price', 'category')  

class CustomerProduct(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','phone', 'email']
    list_filter = ('email', 'last_name')  



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer', 'quantity', 'price', 'date', 'status') 
    list_filter = ('status', 'date')  




