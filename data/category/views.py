from rest_framework import viewsets

from data.category.serializers import CategorySerializer
from data.category.models import Category
from data.common.pagination import CustomPagination


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPagination
