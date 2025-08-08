from django.db import models
from typing import TYPE_CHECKING

from data.common.models import BaseModel

if TYPE_CHECKING:
    from data.customer.models import Customer


class Order(BaseModel):
    STATUS_CHOICES = (
        ("PENDING", "Pending"),  # Buyurtma qabul qilindi
        ("PREPARING", "Preparing"),  # Ovqat tayyorlanmoqda
        ("READY", "Ready for Pickup"),  # Tayyor, olib ketishga/Yetkazib berishga tayyor
        ("ON_THE_WAY", "On the way"),  # Yetkazib berilmoqda
        ("DELIVERED", "Delivered"),  # Yetkazib berildi
        ("CANCELLED", "Cancelled"),  # Bekor qilindi
    )

    customer: "Customer" = models.ForeignKey(
        "customer.Customer",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )
