from django.db import models
import uuid

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=256)
    hash = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.name}"


class Item(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="items")
    code = models.CharField(max_length=256)
    name = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.name} has code: {self.code}"


class Image(models.Model):
    hash = models.CharField(max_length=45)
    extension = models.CharField(max_length=64)
    full = models.CharField(max_length=512)

    def __str__(self):
        return f"{self.full}"
