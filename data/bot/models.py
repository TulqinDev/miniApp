from django.db import models
from typing import TYPE_CHECKING

from data.common.models import BaseModel

if TYPE_CHECKING:
    from data.user.models import User
    from data.customer.models import Customer


class BotUser(BaseModel):
    chat_id = models.BigIntegerField(unique=True)
    tg_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    username = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    user: "User" = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        related_name="bot_users"
    )

    customer: "Customer" = models.ForeignKey(
        "customer.Customer",
        on_delete=models.CASCADE,
        related_name="bot_users",
    )
