from django.contrib import admin

from data.order.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "customer",
        "total_price",
        "payment_method",
        "status",
    )
    list_filter = ("created_at",)
    ordering = ("-created_at",)


