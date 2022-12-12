from django.contrib import admin
from . import models

# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user')

class BookinCartAdmin(admin.ModelAdmin):
    list_display = ('pk', 'book', 'cart', 'quantity', 'price', 'create_date', 'update_date')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'status', 'cart', 'phone', 'name', 'adress', 'email', 'create_date', 'update_date')

admin.site.register(models.Order, OrderAdmin) 
admin.site.register(models.BookinCart, BookinCartAdmin) 
admin.site.register(models.Cart, CartAdmin)