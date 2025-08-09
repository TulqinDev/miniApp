from django.contrib import admin

from data.category.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at",)
    ordering = ("name",)
