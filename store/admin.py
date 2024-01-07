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




