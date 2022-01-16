from rest_framework.routers import DefaultRouter
from products.api.views.products import *

router_products = DefaultRouter()

router_products.register(prefix='products', basename='products', viewset=ProductsModelViewSet)