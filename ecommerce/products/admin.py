from django.contrib import admin
from products.models import Product
from products.models import Customer
# Register your models here.

admin.site.site_header = "Trybe Products Ecommerce"
admin.site.register(Product)
admin.site.register(Customer)
