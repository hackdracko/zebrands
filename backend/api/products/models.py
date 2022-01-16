from django.db import models
import uuid
from django.db.models.fields import DecimalField
from core.abstract_models import DatesModel
from django.conf import settings

class Products(DatesModel):
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sku = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    price = DecimalField(max_digits=9, decimal_places=2)
    brand = models.CharField(max_length=50)

class LogActions(DatesModel):
    class Meta:
        verbose_name = "Log Product"
        verbose_name_plural = "Log Products"

    def __str__(self):
        return self.name

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    action = models.CharField(max_length=20)
    data = models.CharField(max_length=50)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )