from django.contrib import admin
from .models import Product, WhisList  # Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        # 'sku',
        'title',
        'price',
        # 'rating',
        'image',
    )

    # ordening = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class WhisListAdmin(admin.ModelAdmin):
    list_display = (
        'user_profile',
        'product',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(WhisList, WhisListAdmin)
# admin.site.register(Category, CategoryAdmin)
