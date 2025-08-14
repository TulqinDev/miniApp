from rest_framework import viewsets

from data.common.pagination import CustomPagination
from data.deliver.models import Deliver
from data.deliver.serializers import DeliverSerializer


class DeliverViewSet(viewsets.ModelViewSet):
    queryset = Deliver.objects.all()
    serializer_class = DeliverSerializer
    pagination_class = CustomPagination
