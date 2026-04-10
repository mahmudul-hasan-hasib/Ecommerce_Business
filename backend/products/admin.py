from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "stock", "category", "rating", "reviews", "is_featured")
    prepopulated_fields = {"slug": ("name",)}