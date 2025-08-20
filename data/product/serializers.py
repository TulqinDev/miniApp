from rest_framework import serializers
from data.product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id',
            "name",
            "category",
            "picture",
            "price",
            "description"
        )

    def get_category(self, obj):
        return obj.category.name if obj.category else None
