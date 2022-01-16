from rest_framework import serializers
from products.models import *

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'sku', 'name', 'price', 'brand', 'created_at', 'updated_at']

class LogActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogActions
        fields = ['id', 'sku', 'name', 'price', 'brand', 'created_at', 'updated_at']