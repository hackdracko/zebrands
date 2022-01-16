from rest_framework.viewsets import ModelViewSet
from core.pagination import CustomPagination
from products.models import *
from users.models import *
from products.api.serializers import *
from api.permissions import IsAdminOrAnonymous
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from core.smtp import *

class ProductsModelViewSet(ModelViewSet):
    permission_classes = [IsAdminOrAnonymous]
    pagination_class = CustomPagination
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()

    # GET ALL PRODUCTS
    def list(self, request):
        pagination_class = CustomPagination
        data = Products.objects.all()
        paginator = pagination_class()
        result_page = paginator.paginate_queryset(data, request)
        serializer = ProductsSerializer(data, many=True)
        ProductsModelViewSet.save_log(request, 'getAll')
        return paginator.get_paginated_response(serializer.data)

    # GET PRODUCT BY ID
    def retrieve(self, request, pk=None):
        try:
            data = Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            return HttpResponse(status=404)
        serializer = ProductsSerializer(data)
        ProductsModelViewSet.save_log(request, 'getById')
        return JsonResponse(serializer.data)

    # UPDATE PRODUCT BY ID
    def update(self, request, pk=None):
        try:
            product = Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            return HttpResponse(status=404)

        serializer = ProductsSerializer(product, data=request.data) 
        if serializer.is_valid(): 
            serializer.save()
            admins = User.objects.filter(is_staff=1)
            for admin in admins:
                if admin.email:
                    sendNotification(pk, request.user.username, admin.email)
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Saving log in table LogActions
    def save_log(request, desc):
        data = {}
        data['action'] = 'get'
        data['data'] = desc
        data['user'] = request.user.id
        serializer = LogActionsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()