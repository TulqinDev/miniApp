from django.db import models

from data.common.models import BaseModel


class Location(BaseModel):
    latitude = models.FloatField()
    longitude = models.FloatField()
