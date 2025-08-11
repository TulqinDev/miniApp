from django.db import models

from data.common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
