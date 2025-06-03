from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'price'] # Aparece los campos de nombre y precio en el administrador de django.
    search_fields = ['name'] # Agrega un buscador en el administrador de django.

admin.site.register(Product, ProductAdmin)