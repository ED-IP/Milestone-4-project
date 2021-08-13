from django.contrib import admin
from .models import Product # Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        # 'sku',
        'title',
        # 'category',
        'price',
        # 'rating',
        # 'image',
    )

    # ordening = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
# admin.site.register(Category, CategoryAdmin)