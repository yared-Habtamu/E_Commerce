from django.contrib import admin
from .models import Product, Category


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock_quantity')
    search_fields = ('name',)
    ordering = ('-id',)
    list_filter = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
