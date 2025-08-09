from rest_framework import viewsets

from data.category.serializers import CategorySerializer
from data.category.models import Category


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
