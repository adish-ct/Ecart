from django.contrib import admin
from .models import Category, Product


# Register your models here.
# model 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


# model 2
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available']
    list_editable = ['price', 'stock', 'available']
    list_per_page = 20
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
