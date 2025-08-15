from rest_framework.generics import ListCreateAPIView

from data.common.pagination import CustomPagination
from data.order.models import Order
from data.order.serializers import OrderCreateSerializer


class OrderListCreateView(ListCreateAPIView):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderCreateSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Order.objects.all().order_by('-created_at')

        if self.request.role == "CUSTOMER":
            return queryset.filter(customer=self.request.customer)

        # if getattr(self.request, "role", None) == "CUSTOMER":  # Test uchun
        #     return queryset.filter(customer=self.request.customer)

        return queryset
