from django.contrib import admin
from .models import Image, Product, Item
# Register your models here.

admin.site.register([Image, Product, Item])
