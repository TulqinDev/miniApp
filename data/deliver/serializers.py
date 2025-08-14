from rest_framework import serializers

from data.deliver.models import Deliver


class DeliverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliver
        fields = ("id", "name", "phone_number")
