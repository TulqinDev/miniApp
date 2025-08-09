from django.db import models

from data.common.models import BaseModel


class User(BaseModel):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
