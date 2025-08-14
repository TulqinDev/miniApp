from rest_framework import viewsets

from data.common.pagination import CustomPagination
from data.user.models import User
from data.user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination
