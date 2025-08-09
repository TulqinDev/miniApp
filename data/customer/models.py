from django.db import models

from data.common.models import BaseModel


class Customer(BaseModel):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, unique=True)

