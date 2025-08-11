from django.contrib import admin

from data.product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "picture",
        "price",
        "description",
    )

    list_filter = ("category",)

    def get_category(self, obj):
        return obj.category.name
