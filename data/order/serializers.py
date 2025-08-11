from rest_framework import serializers

from data.order.models import Order
from data.order_product.models import OrderProduct
from data.order_product.serializers import OrderProductSerializer


class OrderCreateSerializer(serializers.ModelSerializer):
    customer = serializers.SerializerMethodField()
    products = OrderProductSerializer(many=True)
    total_price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        read_only=True
    )

    class Meta:
        model = Order
        fields = (
            "id",
            "customer",
            "payment_method",
            "products",
            "total_price",
            "status"
        )

    def get_customer(self, obj):
        return obj.customer.name

    def create(self, validated_data):
        products_data = validated_data.pop('products')

        # middleware orqali keladi
        customer = self.context["request"].customer

        if not customer:
            raise serializers.ValidationError("Customer not found in request.")

        total_price = 0

        order = Order.objects.create(customer=customer, **validated_data)

        for item in products_data:
            product = item["product"]
            quantity = item["quantity"]

            total_price += product.price * quantity

            OrderProduct.objects.create(
                order=order,
                product=product,
                quantity=quantity
            )

        order.total_price = total_price
        order.save()
        return order
