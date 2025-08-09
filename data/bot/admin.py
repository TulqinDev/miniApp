from django.contrib import admin

from data.bot.models import BotUser


@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = (
        "tg_name",
        "username",
        "chat_id",
        "user",
        "customer",
    )
    search_fields = (
        "tg_name",
        "username",
    )
    list_filter = ("created_at",)
    ordering = ("-created_at",)
