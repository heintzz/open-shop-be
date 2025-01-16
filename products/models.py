from django.db import models
import uuid

class Product(models.Model):
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  name = models.CharField(max_length=255)
  sku = models.CharField(max_length=255, unique=True)
  description = models.TextField()
  shop = models.CharField(max_length=255)
  location = models.CharField(max_length=255)
  price = models.IntegerField()
  discount = models.IntegerField(default=0)
  category = models.CharField(max_length=255)
  stock = models.IntegerField()
  is_available = models.BooleanField(default=True)
  picture = models.URLField(max_length=2048)