from django.contrib import admin

from data.user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone_number",
        "created_at"
    )
    list_filter = ("created_at",)
    ordering = ("-created_at",)
