from django.contrib import admin
from .models import Product, Category, Review, Cart, Order, OrderItem

# Category Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# Product Admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock_quantity', 'category', 'created_date')
    search_fields = ('name', 'category__name')
    list_filter = ('category', 'price', 'created_date')
    ordering = ('-created_date',)


# Review Admin
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_date')
    search_fields = ('user__username', 'product__name')
    list_filter = ('rating', 'created_date')
    ordering = ('-created_date',)


# Cart Admin
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'added_date')
    search_fields = ('user__username', 'product__name')
    list_filter = ('user', 'added_date')
    ordering = ('-added_date',)


# Order Item Inline Admin
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


# Order Admin
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price', 'created_date')
    search_fields = ('user__username',)
    list_filter = ('created_date',)
    inlines = [OrderItemInline]
    ordering = ('-created_date',)


# Register all models
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
