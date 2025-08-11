from rest_framework.generics import ListCreateAPIView

from data.order.models import Order
from data.order.serializers import OrderCreateSerializer


class OrderListCreateView(ListCreateAPIView):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderCreateSerializer

    def get_queryset(self):
        queryset = Order.objects.all().order_by('-created_at')

        if self.request.role == "CUSTOMER":
            return queryset.filter(customer=self.request.customer)

        return queryset
