from django.contrib import admin

from data.order_product.models import OrderProduct


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "product",
        "quantity",
    )

    list_filter = ("order",)

    ordering = ("order", "-created_at")


