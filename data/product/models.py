from django.db import models
from typing import TYPE_CHECKING

from data.common.models import BaseModel

if TYPE_CHECKING:
    from data.category.models import Category
    from data.file.models import File


class Product(BaseModel):
    name = models.CharField(max_length=120)
    category: "Category" = models.ForeignKey(
        "category.Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products")

    picture: "File" = models.ForeignKey(
        "file.File",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="prodict_pictures")

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    description = models.TextField()


    def __str__(self):
        return f"{self.name} - {self.price}"
