from rest_framework.viewsets import ModelViewSet
from core.pagination import CustomPagination
from users.models import *
from users.serializers import *
from api.permissions import IsAdminOrAnonymous

class UsersModelViewSet(ModelViewSet):
    permission_classes = [IsAdminOrAnonymous]
    pagination_class = CustomPagination
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # http_method_names = ['get']