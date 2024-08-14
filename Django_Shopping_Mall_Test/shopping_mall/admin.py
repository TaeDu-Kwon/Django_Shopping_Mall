from django.contrib import admin

# Register your models here.
# admin 0000

from .models import Product_Info,Cart,CartItem

admin.site.register(Product_Info)
admin.site.register(Cart)
admin.site.register(CartItem)