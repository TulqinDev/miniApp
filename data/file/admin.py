from django.contrib import admin

from data.file.models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ("file", "created_at")
