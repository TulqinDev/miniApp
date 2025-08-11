from rest_framework.urls import path

from data.order.views import OrderListCreateView

urlpatterns = [
    path("", OrderListCreateView.as_view())  # Create order and get Order list
]
