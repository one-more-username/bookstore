from django.contrib import admin

from .models import ShoppingCart, BookForBuy

# Register your models here.

admin.site.register(ShoppingCart)
admin.site.register(BookForBuy)
