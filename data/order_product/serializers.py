from rest_framework import serializers

from data.order_product.models import OrderProduct
from data.product.models import Product


class OrderProductSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source="order_products"
    )

    class Meta:
        model = OrderProduct
        fields = ("product", "quantity")