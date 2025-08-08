from django.db import models
from typing import TYPE_CHECKING

from data.common.models import BaseModel

if TYPE_CHECKING:
    from data.order.models import Order
    from data.product.models import Product


class OrderProduct(BaseModel):
    order: "Order" = models.ForeignKey(
        "order.Order",
        on_delete=models.CASCADE,
        related_name="products",
    )

    product: "Product" = models.ForeignKey(
        "product.Product",
        on_delete=models.CASCADE,
        related_name="order_products",
    )

    quantity = models.PositiveIntegerField(default=1)
