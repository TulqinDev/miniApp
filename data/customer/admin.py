from django.contrib import admin

from data.customer.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone_number",
        "created_at",
    )
    list_filter = ("created_at",)
    ordering = ("-created_at",)
    search_fields = (
        "name",
        "phone_number",
    )
