from django.db import models

from data.common.models import BaseModel


class Category(BaseModel):
    name_uz = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
