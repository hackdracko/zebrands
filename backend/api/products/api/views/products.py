from rest_framework.viewsets import ModelViewSet
from core.pagination import CustomPagination
from products.models import *
from products.api.serializers import *

class ProductsModelViewSet(ModelViewSet):
    pagination_class = CustomPagination
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    # http_method_names = ['get']