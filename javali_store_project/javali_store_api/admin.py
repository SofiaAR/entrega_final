from django.contrib import admin

# Register your models here.

from .models import Product, Sale, Category, SaleProduct, Store, Contact, Brand

admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Category)
admin.site.register(SaleProduct)
admin.site.register(Store)
admin.site.register(Contact)
admin.site.register(Brand)
